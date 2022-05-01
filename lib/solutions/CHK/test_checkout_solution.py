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
    # def test_checkout(self):
    #     sku1 = '''ABCD'''
    #     sku2 = '''ABCD2'''
    #     sku3 = ''''''
    #     sku4 = '''AABABD'''
    #     sku5 = '''ZMJSD'''
    #     sku6 = '''AAAAAA'''
    #     sku7 = '''AAAEE'''
    #     sku8 = '''a'''
    #     sku9 = '''AAAAAAAAAAAAA'''
    #     sku10 = '''EEEBB'''
    #     sku11 ='''EEB'''
    #     sku12 ='''EEEB'''
    #     sku13 = '''EEEEBB'''
    #     sku14 = '''EEEEEEEEBBBB'''

    #     self.assertEqual(checkout(sku1), 115)
    #     self.assertEqual(checkout(sku2), -1)
    #     self.assertEqual(checkout(sku3), 0)
    #     self.assertEqual(checkout(sku4), 190)
    #     self.assertEqual(checkout(sku5), -1)
    #     self.assertEqual(checkout(sku6), 250)
    #     self.assertEqual(checkout(sku7), 210)

    #     self.assertEqual(checkout(sku8), -1)
    #     self.assertEqual(checkout(sku9), 530)
    #     self.assertEqual(checkout(sku10), 150)
    #     self.assertEqual(checkout(sku11), 80)
    #     self.assertEqual(checkout(sku12), 120)
    #     self.assertEqual(checkout(sku13), 160)
    #     self.assertEqual(checkout(sku14), 320)

    #round 3
    # def test_checkout(self):
    #     sku1 = '''ABCD'''
    #     sku2 = '''ABCD2'''
    #     sku3 = ''''''
    #     sku4 = '''AABABD'''
    #     sku5 = '''ZMJSD'''
    #     sku6 = '''AAAAAA'''
    #     sku7 = '''AAAEE'''
    #     sku8 = '''a'''
    #     sku9 = '''AAAAAAAAAAAAA'''
    #     sku10 = '''EEEBB'''
    #     sku11 ='''EEB'''
    #     sku12 ='''EEEB'''
    #     sku13 = '''EEEEBB'''
    #     sku14 = '''EEEEEEEEBBBB'''
    #     sku15 = '''FFF'''
    #     sku16 = '''EEEBBFFFFFF'''
    #     sku17 = '''ABCDEF'''

    #     self.assertEqual(checkout(sku1), 115)
    #     self.assertEqual(checkout(sku2), -1)
    #     self.assertEqual(checkout(sku3), 0)
    #     self.assertEqual(checkout(sku4), 190)
    #     self.assertEqual(checkout(sku5), -1)
    #     self.assertEqual(checkout(sku6), 250)
    #     self.assertEqual(checkout(sku7), 210)

    #     self.assertEqual(checkout(sku8), -1)
    #     self.assertEqual(checkout(sku9), 530)
    #     self.assertEqual(checkout(sku10), 150)
    #     self.assertEqual(checkout(sku11), 80)
    #     self.assertEqual(checkout(sku12), 120)
    #     self.assertEqual(checkout(sku13), 160)
    #     self.assertEqual(checkout(sku14), 320)

    #     self.assertEqual(checkout(sku15), 20)
    #     self.assertEqual(checkout(sku16), 190)
    #     self.assertEqual(checkout(sku17), 165)
    
    #round 4
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
        sku14 = '''EEEEEEEEBBBB'''
        sku15 = '''FFF'''
        sku16 = '''EEEBBFFFFFF'''
        sku17 = '''ABCDEF'''

        self.assertEqual(checkout(sku1), 115)
        self.assertEqual(checkout(sku2), -1)
        self.assertEqual(checkout(sku3), 0)
        self.assertEqual(checkout(sku4), 190)
        self.assertEqual(checkout(sku5), -1)
        self.assertEqual(checkout(sku6), 250)
        self.assertEqual(checkout(sku7), 210)

        self.assertEqual(checkout(sku8), -1)
        self.assertEqual(checkout(sku9), 530)
        self.assertEqual(checkout(sku10), 150)
        self.assertEqual(checkout(sku11), 80)
        self.assertEqual(checkout(sku12), 120)
        self.assertEqual(checkout(sku13), 160)
        self.assertEqual(checkout(sku14), 320)

        self.assertEqual(checkout(sku15), 20)
        self.assertEqual(checkout(sku16), 190)
        self.assertEqual(checkout(sku17), 165)
    
    def test_totalValueOfBs(self):
        self.assertEqual(totalValueOfBs(2), 45)
        self.assertEqual(totalValueOfBs(3), 75)
        self.assertEqual(totalValueOfBs(4), 90)

    def test_totalValueOfAs(self):
        self.assertEqual(totalValueOfAs(2), 100)
        self.assertEqual(totalValueOfAs(3), 130)
        self.assertEqual(totalValueOfAs(5), 200)
        self.assertEqual(totalValueOfAs(13), 530)

    def test_totalValueOfFs(self):
        self.assertEqual(totalValueOfFs(5), 40)
        self.assertEqual(totalValueOfFs(2), 20)
        self.assertEqual(totalValueOfFs(6), 40)
    
    def test_updateCounterDict(self):
        dict1={'E':2, 'B':1}
        dict2={'E':2, 'B':0}
        dict3={'F':6, 'B':1}
        dict4={'F':4, 'B':1}
        self.assertEqual(updateCounterDict(dict1), dict2)
        self.assertEqual(updateCounterDict(dict3), dict4)
    

if __name__ == '__main__':
    unittest.main()

