import unittest
from checkout_solution import *



class TestSolution(unittest.TestCase):
    def test_checkout(self):
        sku1 = '''abcd'''
        sku2 = '''abcd2'''
        sku3 = ''''''
        sku4 = '''aababd'''
        sku5 = '''zmjsd'''
        sku6 = '''aababdaaaaaac'''
        sku7 = '''AA'''
        self.assertEqual(checkout(sku1), 115)
        self.assertEqual(checkout(sku2), -1)
        self.assertEqual(checkout(sku3), -1)
        self.assertEqual(checkout(sku4), 190)
        self.assertEqual(checkout(sku5), -1)
        self.assertEqual(checkout(sku6), 470)
        self.assertEqual(checkout(sku7), 100)


if __name__ == '__main__':
    unittest.main()