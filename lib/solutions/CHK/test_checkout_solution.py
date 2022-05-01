import unittest
from checkout_solution import *



class TestSolution(unittest.TestCase):
    def test_checkout(self):
        sku1 = '''ABCD'''
        sku2 = '''ABCD2'''
        sku3 = ''''''
        sku4 = '''AABABD'''
        sku5 = '''ZMJSD'''
        sku6 = '''AABABDAAAAAAC'''
        sku7 = '''AA'''
        sku8 = '''a'''
        self.assertEqual(checkout(sku1), 115)
        self.assertEqual(checkout(sku2), -1)
        self.assertEqual(checkout(sku3), 0)
        self.assertEqual(checkout(sku4), 190)
        self.assertEqual(checkout(sku5), -1)
        self.assertEqual(checkout(sku6), 470)
        self.assertEqual(checkout(sku7), 100)
        self.assertEqual(checkout(sku8), -1)


if __name__ == '__main__':
    unittest.main()

