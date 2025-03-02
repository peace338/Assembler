import logging

logger = logging.getLogger(__name__)

class SymbolTable():
    def __init__(self):
        """
        Creates a new empty symbol table
        """
        self._symbolTable = {"R0"       : 0,
                             "R1"       : 1,
                             "R2"       : 2,
                             "R3"       : 3,
                             "R4"       : 4,
                             "R5"       : 5,
                             "R6"       : 6,
                             "R7"       : 7,
                             "R8"       : 8,
                             "R9"       : 9,
                             "R10"      : 10,
                             "R11"      : 11,
                             "R12"      : 12,
                             "R13"      : 13,
                             "R14"      : 14,
                             "R15"      : 15,
                             "SP"       : 0,
                             "LCL"      : 1,
                             "ARG"      : 2,
                             "THIS"     : 3,
                             "THAT"     : 4,
                             "SCREEN"   : 16384,
                             "KBD"      : 24576,
        }

    def addEntry(self, symbol: str, address: int):
        """
        Adds the pair (symbol, address) to the table.
        """
        logger.debug("new symbol {} is added at {}".format(symbol, address))
        self._symbolTable[symbol] = address

    def contains(self, symbol: str) -> bool:
        """
        Does the symbol table contain the given symbol?
        """
        return True if symbol in self._symbolTable else False

    def getAddress(self, symbol: str) -> int:
        """
        Returns the address associated with the symbol.
        """
        return self._symbolTable[symbol]