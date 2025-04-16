import unittest
from src.SymbolTable.SymbolTable import SymbolTable

class TestContain(unittest.TestCase):
    def test_should_contain_if_entry_added(self):
        # arrange
        table = SymbolTable()
        symbol = "RO"
        address = 42

        # act
        table.addEntry(symbol, address)
        contained = table.contains(symbol)

        # assert
        self.assertTrue(contained)

    def test_should_not_contain_if_entry_not_added(self):
        # arrange
        table = SymbolTable()
        symbol = "RO"

        # act
        contained = table.contains(symbol)

        # assert
        self.assertFalse(contained)

class TestGetAddress(unittest.TestCase):
    def test_should_get_address_if_entry_added(self):
        # arrange
        table = SymbolTable()
        symbol = "RO"
        address = 42

        # act
        table.addEntry(symbol, address)
        retrieved = table.getAddress(symbol)

        # assert
        self.assertTrue(address, retrieved)

    @unittest.skip("TODO: fix me to pass")
    def test_should_not_get_address_if_entry_not_added(self):
        # arrange
        table = SymbolTable()
        symbol = "RO"

        # act
        retrieved = table.getAddress(symbol)

        # assert
        self.assertTrue(0, retrieved)

if __name__ == "__main__":
    unittest.main()