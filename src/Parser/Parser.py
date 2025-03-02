from .CommandType import CommandType
import os
import sys
import logging

logger = logging.getLogger(__name__)
class Parser():
    def __init__(self, input_path: str):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        self.__validateInput(input_path)
        self._file = open(input_path, 'rb')
        self._fileSize = os.path.getsize(input_path)
        self.currentCommand = None
        self.currentCommandType = None

    def __del__(self):
        if self._file:
            self._file.close()

    def hasMoreCommands(self) -> bool:
        """
        Are there more commands in the input?
        """
        logger.debug("file pointer: {}/{}".format(self._file.tell(), self._fileSize))
        return self._file.tell() < self._fileSize

    def advance(self):
        """
        Reads the next command from the input and makes it the current command. 
        Should be called only if hasMoreCommands() is true.
        Initially there is no current command.
        """
        logger.debug("Parser.advance() is called.")
        
        while self.hasMoreCommands():

            logger.debug("filePointer before readline: {}/{}".format(self._file.tell(),self._fileSize))
            buffer = self._file.readline().decode("utf-8")
            logger.debug("read line: {} \t|size: {}".format(repr(buffer), len(buffer)))
            logger.debug("file pointer after readline: {}/{}".format(self._file.tell(), self._fileSize))

            if self.__isCommand(buffer):
                logger.debug("peak command: {}".format(buffer))
                self.currentCommand = buffer.rstrip("\n").rstrip()
                self.currentCommandType = self.commandType()
                break

    def commandType(self) -> CommandType:
        """
        Returns the type of the current command:
        - A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        - C_COMMAND for dest=comp;jump
        - L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx is a symbol.
        """

        if self.currentCommand.startswith("@"):
            return CommandType.A_COMMAND
        elif self.currentCommand.startswith("(") and self.currentCommand.endswith(")"):
            return CommandType.L_COMMAND
        else:
            return CommandType.C_COMMAND

    def symbol(self) -> str:
        """
        Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). 
        Should be called only when commandType() is A_COMMAND or L_COMMAND.
        """

        logger.debug("call Parser.symbol()")
        logger.debug("currentCommand: {}".format(self.currentCommandType))
        if self.currentCommandType == CommandType.A_COMMAND:
            return self.currentCommand[1:]
        elif self.currentCommandType == CommandType.L_COMMAND:
            return self.currentCommand[1:-1]
        
    def dest(self) -> str:
        """
        Returns the dest mnemonic in the current C-command (8 possibilities). 
        Should be called only when commandType() is C_COMMAND
        """
        if "=" in self.currentCommand:
            retVal = self.currentCommand.split("=")[0]
        else:
            retVal = 'null'

        return retVal

    def comp(self) -> str:
        """
        Returns the comp mnemonic in the current C-command (28 possibilities). 
        Should be called only when commandType() is C_COMMAND.
        """
        hasEq = "=" in self.currentCommand
        hasSemi = ";" in self.currentCommand

        logger.debug("export comp instruction")
        logger.debug("hasEq: {}, hasSemi: {}".format(hasEq, hasSemi))

        if hasEq and hasSemi:
            retVal = self.currentCommand.split("=")[-1].split(";")[0]
        elif hasEq:
            retVal = self.currentCommand.split("=")[-1]
        elif hasSemi:
            retVal = self.currentCommand.split(";")[0]
        else:
            logger.warning("C_COMMAND must have `=` or `;`.")
            sys.exit(1)
        logger.debug("comp: {}".format(retVal))

        return retVal

    def jump(self) -> str:
        """
        Returns the jump mnemonic in the current C-command (8 possibilities). 
        Should be called only when commandType() is C_COMMAND.
        """
        if ";" in self.currentCommand:
            retVal = self.currentCommand.split(";")[-1]
        else:
            retVal = 'null'

        return retVal

    def __validateInput(self, input_path: str): 

        if os.path.exists(input_path):
            pass
        else:
            print("The file does not exist in the {}".format(input_path), file=sys.stderr)
            sys.exit(1) 

    def __isCommand(self, line: str) -> bool:

        isComment = line.lstrip().startswith("//")
        isSpace = line.isspace()

        if isComment or isSpace:
            logger.debug("this line is not a command. [isComment, isSpace]: {}, {}".format(isComment, isSpace))
            retVal = False
        else:
            logger.debug("this line is a command")
            retVal = True

        return retVal