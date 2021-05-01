import unittest
from vending_machine import VendingMachine


class MyTestCase(unittest.TestCase):

    def test_case1(self):
        vm = VendingMachine()
        result = vm.checkStatus()
        self.assertEqual("Empty VM Started", result)

    def test_case2(self):
        vm = VendingMachine()
        result = vm.checkStock("Coke")
        self.assertEqual("Coke (0)", result)
        result = vm.checkStatus()
        self.assertEqual("Empty VM Started", result)

    def test_case3(self):
        vm = VendingMachine()
        result = vm.checkStock("Orange Juice")
        self.assertEqual("Orange Juice (0)", result)
        result = vm.checkStatus()
        self.assertEqual("Empty VM Started", result)

    def test_case4(self):
        vm = VendingMachine()
        result = vm.checkStock("Kitkat Chunky Bar")
        self.assertEqual("Kitkat Chunky Bar (0)", result)
        result = vm.checkStatus()
        self.assertEqual("Empty VM Started", result)

    def test_case5(self):
        vm = VendingMachine()
        result = vm.checkStock("Lays BBQ Chips")
        self.assertEqual("Invalid product: Lays BBQ Chips", result)
        result = vm.checkStatus()
        self.assertEqual("Empty VM Started", result)

    def test_case6(self):
        vm = VendingMachine()
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

    def test_case7(self):
        vm = VendingMachine()

        vm.add("Coke", 5)

        result = vm.checkStatus()
        self.assertEqual("Product added: Coke (5)", result)

        result = vm.checkStock("Coke")
        self.assertEqual("Coke (5)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (5), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

        vm.add("Orange Juice", 5)

        result = vm.checkStatus()
        self.assertEqual("Product added: Orange Juice (5)", result)

        result = vm.checkStock("Orange Juice")
        self.assertEqual("Orange Juice (5)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (5), Orange Juice (5), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

        vm.add("Kitkat Chunky Bar", 5)

        result = vm.checkStatus()
        self.assertEqual("Product added: Kitkat Chunky Bar (5)", result)

        result = vm.checkStock("Kitkat Chunky Bar")
        self.assertEqual("Kitkat Chunky Bar (5)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (5), Orange Juice (5), Kitkat Chunky Bar (5), Lays Classic Chips (0)", result)

        vm.add("Lays Classic Chips", 5)

        result = vm.checkStatus()
        self.assertEqual("Product added: Lays Classic Chips (5)", result)

        result = vm.checkStock("Lays Classic Chips")
        self.assertEqual("Lays Classic Chips (5)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (5), Orange Juice (5), Kitkat Chunky Bar (5), Lays Classic Chips (5)", result)

        vm.add("Maltesers Chocolate", 4)

        result = vm.checkStatus()
        self.assertEqual("Invalid product: Maltesers Chocolate", result)

        result = vm.checkStock("Maltesers Chocolate")
        self.assertEqual("Invalid product: Maltesers Chocolate", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (5), Orange Juice (5), Kitkat Chunky Bar (5), Lays Classic Chips (5)", result)

    def test_case8(self):
        vm = VendingMachine()

        vm.add("Coke", 5)
        vm.add("Orange Juice", 6)
        vm.add("Kitkat Chunky Bar", 7)
        vm.add("Lays Classic Chips", 8)
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (5), Orange Juice (6), Kitkat Chunky Bar (7), Lays Classic Chips (8)", result)

        vm.dispense("Coke", 1)

        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (1)", result)

        result = vm.checkStock("Coke")
        self.assertEqual("Coke (4)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (4), Orange Juice (6), Kitkat Chunky Bar (7), Lays Classic Chips (8)", result)

        vm.dispense("Orange Juice", 2)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Orange Juice (2)", result)

        result = vm.checkStock("Orange Juice")
        self.assertEqual("Orange Juice (4)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (4), Orange Juice (4), Kitkat Chunky Bar (7), Lays Classic Chips (8)", result)

        vm.dispense("Kitkat Chunky Bar", 3)

        result = vm.checkStatus()
        self.assertEqual("Product removed: Kitkat Chunky Bar (3)", result)

        result = vm.checkStock("Kitkat Chunky Bar")
        self.assertEqual("Kitkat Chunky Bar (4)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (4), Orange Juice (4), Kitkat Chunky Bar (4), Lays Classic Chips (8)", result)

        vm.dispense("Lays Classic Chips", 4)

        result = vm.checkStatus()
        self.assertEqual("Product removed: Lays Classic Chips (4)", result)
        result = vm.checkStock("Lays Classic Chips")
        self.assertEqual("Lays Classic Chips (4)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (4), Orange Juice (4), Kitkat Chunky Bar (4), Lays Classic Chips (4)", result)

        vm.dispense("M & M's Chocoloate Bag", 4)

        result = vm.checkStatus()
        self.assertEqual("Invalid product: M & M's Chocoloate Bag", result)

        result = vm.checkStock("M & M's Chocoloate Bag")
        self.assertEqual("Invalid product: M & M's Chocoloate Bag", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (4), Orange Juice (4), Kitkat Chunky Bar (4), Lays Classic Chips (4)", result)

    def test_case9(self):
        vm = VendingMachine()

        vm.add("Kitkat Chunky Bar", 7)
        self.assertEqual("Kitkat Chunky Bar (7)", vm.checkStock("Kitkat Chunky Bar"))
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (7), Lays Classic Chips (0)",
                         vm.checkStock())

        vm.dispense("Kitkat Chunky Bar", 3)
        self.assertEqual("Kitkat Chunky Bar (4)", vm.checkStock("Kitkat Chunky Bar"))
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (4), Lays Classic Chips (0)",
                         vm.checkStock())

        vm.add("Kitkat Chunky Bar", 5)
        self.assertEqual("Kitkat Chunky Bar (9)", vm.checkStock("Kitkat Chunky Bar"))
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (9), Lays Classic Chips (0)",
                         vm.checkStock())

    def test_case10(self):
        vm = VendingMachine()

        vm.add("Coke", 5)

        result = vm.checkStatus()
        self.assertEqual("Product added: Coke (5)", result)

        result = vm.checkStock("Coke")
        self.assertEqual("Coke (5)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (5), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

        vm.add("Coke", 19)
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (24), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)
        result = vm.checkStatus()
        self.assertEqual("Product added: Coke (19)", result)

        vm.dispense("Coke", 3)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (3)", result)
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (21), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

    def test_case11(self):
        vm = VendingMachine()

        vm.add("Coke", 9)

        result = vm.checkStatus()
        self.assertEqual("Product added: Coke (9)", result)

        result = vm.checkStock("Coke")
        self.assertEqual("Coke (9)", result)

        result = vm.checkStock("Orange Juice")
        self.assertEqual("Orange Juice (0)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (9), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

        vm.add("Kitkat Chunky Bar", 6)

        result = vm.checkStatus()
        self.assertEqual("Product added: Kitkat Chunky Bar (6)", result)

        result = vm.checkStock("Kitkat Chunky Bar")
        self.assertEqual("Kitkat Chunky Bar (6)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (9), Orange Juice (0), Kitkat Chunky Bar (6), Lays Classic Chips (0)", result)

        vm.dispense("Coke", 3)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (3)", result)
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (6), Orange Juice (0), Kitkat Chunky Bar (6), Lays Classic Chips (0)", result)

    def test_case12(self):
        vm = VendingMachine()

        vm.add("Coke", 9)

        result = vm.checkStatus()
        self.assertEqual("Product added: Coke (9)", result)

        result = vm.checkStock("Coke")
        self.assertEqual("Coke (9)", result)

        result = vm.checkStock("Orange Juice")
        self.assertEqual("Orange Juice (0)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (9), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

        vm.add("Kitkat Chunky Bar", 6)

        result = vm.checkStatus()
        self.assertEqual("Product added: Kitkat Chunky Bar (6)", result)

        result = vm.checkStock("Kitkat Chunky Bar")
        self.assertEqual("Kitkat Chunky Bar (6)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (9), Orange Juice (0), Kitkat Chunky Bar (6), Lays Classic Chips (0)", result)

        vm.dispense("Coke", 3)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (3)", result)
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (6), Orange Juice (0), Kitkat Chunky Bar (6), Lays Classic Chips (0)", result)

        vm.dispense("Kitkat Chunky Bar", 6)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Kitkat Chunky Bar (6)", result)

        vm.dispense("Coke", 2)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (2)", result)
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (4), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

        vm.dispense("Coke", 4)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (4)", result)

        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (4)", result)

        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (4)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

    def test_case13(self):
        vm = VendingMachine()

        vm.add("Coke", 9)

        result = vm.checkStatus()
        self.assertEqual("Product added: Coke (9)", result)

        result = vm.checkStock("Coke")
        self.assertEqual("Coke (9)", result)

        result = vm.checkStock("Orange Juice")
        self.assertEqual("Orange Juice (0)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (9), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

        vm.add("Kitkat Chunky Bar", 6)

        result = vm.checkStatus()
        self.assertEqual("Product added: Kitkat Chunky Bar (6)", result)

        result = vm.checkStock("Kitkat Chunky Bar")
        self.assertEqual("Kitkat Chunky Bar (6)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (9), Orange Juice (0), Kitkat Chunky Bar (6), Lays Classic Chips (0)", result)

        vm.dispense("Coke", 3)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (3)", result)
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (6), Orange Juice (0), Kitkat Chunky Bar (6), Lays Classic Chips (0)", result)

        vm.dispense("Kitkat Chunky Bar", 6)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Kitkat Chunky Bar (6)", result)

        vm.dispense("Coke", 2)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (2)", result)
        result = vm.checkStock()
        self.assertEqual("Stock: Coke (4), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

        vm.dispense("Coke", 4)
        result = vm.checkStatus()
        self.assertEqual("Product removed: Coke (4)", result)

        result = vm.checkStock()
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)", result)

    def test_case15(self):
        vm = VendingMachine()

        vm.add("Pepsi", 7)
        self.assertEqual("Invalid product: Pepsi", vm.checkStock("Pepsi"))
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (0), Lays Classic Chips (0)",
                         vm.checkStock())

        vm.add("Kitkat Chunky Bar", 102)
        self.assertEqual("Kitkat Chunky Bar (102)", vm.checkStock("Kitkat Chunky Bar"))
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (102), Lays Classic Chips (0)",
                         vm.checkStock())

        vm.dispense("Kitkat Chunky Bar", 99)
        self.assertEqual("Kitkat Chunky Bar (3)", vm.checkStock("Kitkat Chunky Bar"))
        self.assertEqual("Stock: Coke (0), Orange Juice (0), Kitkat Chunky Bar (3), Lays Classic Chips (0)",
                         vm.checkStock())


if __name__ == '__main__':
    unittest.main()
