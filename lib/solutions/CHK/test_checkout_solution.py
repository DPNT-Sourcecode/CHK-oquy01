import unittest
from checkout_solution import *



class TestSolution(unittest.TestCase):
    #Round 1
    # def test_checkout(self):
    #     sku1 = '''ABCD'''
    #     sku2 = '''ABCD2'''
    #     sku3 = ''''''
    #     sku4 = '''AABABD'''
    #     sku5 = '''ZMJSD'''
    #     sku6 = '''AABABDAAAAAAC'''
    #     sku7 = '''AA'''
    #     sku8 = '''a'''
    #     sku9 = '''BBBB'''
    #     self.assertEqual(checkout(sku1), 115)
    #     self.assertEqual(checkout(sku2), -1)
    #     self.assertEqual(checkout(sku3), 0)
    #     self.assertEqual(checkout(sku4), 190)
    #     self.assertEqual(checkout(sku5), -1)
    #     self.assertEqual(checkout(sku6), 470)
    #     self.assertEqual(checkout(sku7), 100)
    #     self.assertEqual(checkout(sku8), -1)
    #     self.assertEqual(checkout(sku9), 90)
    
    #Round 2
    def test_checkout(self):
        sku1 = '''ABCD'''
        sku2 = '''ABCD2'''
        sku3 = ''''''
        sku4 = '''AABABD'''
        sku5 = '''ZMJSD'''
        sku6 = '''AAAAAA'''
        sku7 = '''AAAEE'''
        sku8 = '''a'''
        sku9 = '''AAAAAAAAAAAAA'''
        sku9 = '''EBAAAAAAAAAAAAA'''
        sku9 = '''EEEBB'''
        self.assertEqual(checkout(sku1), 115)
        self.assertEqual(checkout(sku2), -1)
        self.assertEqual(checkout(sku3), 0)
        self.assertEqual(checkout(sku4), 190)
        self.assertEqual(checkout(sku5), -1)
        self.assertEqual(checkout(sku6), 250)
        self.assertEqual(checkout(sku7), 210)

        self.assertEqual(checkout(sku8), -1)
        self.assertEqual(checkout(sku9), 165)


if __name__ == '__main__':
    unittest.main()



