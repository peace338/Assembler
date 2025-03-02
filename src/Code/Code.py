from .CodeTable import *
class Code():
    def __init__(self):
        pass

    def dest(self, mnemonic: str) -> int: #3bit
        """
        Returns the binary code of the dest mnemonic.
        """
        return destTable[mnemonic]

    def comp(self, mnemonic: str) -> int: #7bit
        """
        Returns the binary code of the comp mnemonic.
        """
        return compTable[mnemonic]

    def jump(self, mnemonic: str) -> int: #3bit
        """
        Returns the binary code of the jump mnemonic.
        """
        return jumpTable[mnemonic]


