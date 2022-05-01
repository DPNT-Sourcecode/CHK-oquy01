import unittest
from checkout_solution import *



class TestSolution(unittest.TestCase):
    def test_checkout(self):
        sku1 = '''abcd'''
        self.assertEqual(checkout(sku1), 115)

if __name__ == '__main__':
    unittest.main()