from .CommandType import CommandType
import os
import sys
import re
class Parser():
    def __init__(self, input_path: str):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        self.__validateInput(input_path)
        self.__file = open(input_path, 'r')
        self.__fileSize = os.path.getsize(input_path)
        self.currentCommand = None
        self.currentCommandType = None

    def __del__(self):
        if self.__file:
            self.__file.close()

    def hasMoreCommands(self) -> bool:
        """
        Are there more commands in the input?
        """
        return self.__file.tell() < self.__fileSize

    def advance(self):
        """
        Reads the next command from the input and makes it the current command. 
        Should be called only if hasMoreCommands() is true.
        Initially there is no current command.
        """

        while self.hasMoreCommands():
            
            buffer = self.__file.readline()
            if self.__isCommand(buffer):
                self.currentCommand = buffer.rstrip("\n")
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
        if hasEq and hasSemi:
            retVal = self.currentCommand.split("=")[-1].split(";")[0]
        elif hasEq:
            retVal = self.currentCommand.split("=")[-1]
        elif hasSemi:
            retVal = self.currentCommand.split(";")[0]
        else:
            print("C_COMMAND must have `=` or `;`.")
            sys.exit(1)
        
        return retVal

    def jump(self) -> str:
        """
        Returns the jump mnemonic in the current C-command (8 possibilities). 
        Should be called only when commandType() is C_COMMAND.
        """
        if ";" in self.currentCommand:
            retVal = self.currentCommand.split("=")[-1]
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

        return False if line.lstrip().startswith("//") or line.isspace() else True