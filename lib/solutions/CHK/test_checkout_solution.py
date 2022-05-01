import unittest
from checkout_solution import *



class TestSolution(unittest.TestCase):
    def test_checkout(self):
        sku1 = '''abcd'''
        sku2 = '''abcd2'''
        sku3 = ''''''
        sku4 = '''aababd'''
        self.assertEqual(checkout(sku1), 115)
        self.assertEqual(checkout(sku2), -1)
        self.assertEqual(checkout(sku3), -1)
        self.assertEqual(checkout(sku4), -1)

if __name__ == '__main__':
    unittest.main()