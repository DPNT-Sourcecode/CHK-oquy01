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
        sku10 = '''EEEBB'''
        sku11 ='''EEB'''
        sku12 ='''EEEB'''
        sku13 = '''EEEEBB'''

        self.assertEqual(checkout(sku1), 115)
        self.assertEqual(checkout(sku2), -1)
        self.assertEqual(checkout(sku3), 0)
        self.assertEqual(checkout(sku4), 190)
        self.assertEqual(checkout(sku5), -1)
        self.assertEqual(checkout(sku6), 250)
        self.assertEqual(checkout(sku7), 210)

        self.assertEqual(checkout(sku8), -1)
        self.assertEqual(checkout(sku9), 530)
        self.assertEqual(checkout(sku10), 165)
    
    def test_totalValueOfBs(self):
        self.assertEqual(totalValueOfBs(2), 45)
        self.assertEqual(totalValueOfBs(3), 75)
        self.assertEqual(totalValueOfBs(4), 90)

    def test_totalValueOfAs(self):
        self.assertEqual(totalValueOfAs(2), 100)
        self.assertEqual(totalValueOfAs(3), 130)
        self.assertEqual(totalValueOfAs(5), 200)
        self.assertEqual(totalValueOfAs(13), 530)
    


if __name__ == '__main__':
    unittest.main()




