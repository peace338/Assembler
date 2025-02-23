class SymbolTable():
    def __init__(self):
        """
        Creates a new empty symbol table
        """
        pass

    def addEntry(self, symbol: str, address: int):
        """
        Adds the pair (symbol, address) to the table.
        """
        pass

    def contains(self, symbol: str) -> bool:
        """
        Does the symbol table contain the given symbol?
        """
        pass

    def getAddress(self, symbol: str) -> int:
        """
        Returns the address associated with the symbol.
        """
        pass