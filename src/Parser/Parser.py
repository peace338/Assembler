from .CommandType import CommandType


class Parser():
    def __init__(self, input_path: str):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        pass

    def hasMoreCommands(self,) -> bool:
        """
        Are there more commands in the input?
        """
        pass

    def advance(self):
        """
        Reads the next command from the input and makes it the current command. 
        Should be called only if hasMoreCommands() is true.
        Initially there is no current command.
        """
        pass

    def commandType(self) -> CommandType:
        """
        Returns the type of the current command:
        - A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        - C_COMMAND for dest=comp;jump
        - L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx is a symbol.
        """
        pass

    def symbol(self) -> str:
        """
        Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). 
        Should be called only when commandType() is A_COMMAND or L_COMMAND.
        """
        pass

    def dest(self) -> str:
        """
        Returns the dest mnemonic in the current C-command (8 possibilities). 
        Should be called only when commandType() is C_COMMAND
        """
        pass

    def comp(self) -> str:
        """
        Returns the comp mnemonic in the current C-command (28 possibilities). 
        Should be called only when commandType() is C_COMMAND.
        """
        pass

    def jump(self) -> str:
        """
        Returns the jump mnemonic in the current C-command (8 possibilities). 
        Should be called only when commandType() is C_COMMAND.
        """
        pass
