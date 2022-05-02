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
    #     sku18 = '''UUUUNNNM'''
    #     sku19 = '''VVQ'''
    #     sku20 = '''KKKKL'''
    #     sku21 = '''O'''
    #     sku22 = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    #     sku23 = '''ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'''

    #     self.assertEqual(checkout(sku1), 115)
    #     self.assertEqual(checkout(sku2), -1)
    #     self.assertEqual(checkout(sku3), 0)
    #     self.assertEqual(checkout(sku4), 190)
    #     self.assertEqual(checkout(sku5), 170)
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
    #     self.assertEqual(checkout(sku18), 240)
    #     self.assertEqual(checkout(sku19), 120)
    #     self.assertEqual(checkout(sku20), 390)
    #     self.assertEqual(checkout(sku21), 10)
    #     self.assertEqual(checkout(sku22), 965)
    #     self.assertEqual(checkout(sku23), 1880)
    
    #round 5
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
        sku18 = '''UUUUNNNM'''
        sku19 = '''VVQ'''
        sku20 = '''KKKKL'''
        sku21 = '''O'''
        sku22 = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
        sku23 = '''ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'''
        sku24 = '''STXYZ'''
        sku25 = '''STXYZSTXYZ'''
        sku26 = '''SSSSSSSSSSZ'''
        sku27 = '''STXYZSTXYZSTXYZ'''

        self.assertEqual(checkout(sku1), 115)
        self.assertEqual(checkout(sku2), -1)
        self.assertEqual(checkout(sku3), 0)
        self.assertEqual(checkout(sku4), 190)
        self.assertEqual(checkout(sku5), 131)
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
        self.assertEqual(checkout(sku18), 240)
        self.assertEqual(checkout(sku19), 120)
        self.assertEqual(checkout(sku20), 330)
        self.assertEqual(checkout(sku21), 10)
        self.assertEqual(checkout(sku22), 837)
        self.assertEqual(checkout(sku23), 1602)
        self.assertEqual(checkout(sku24), 82)
        self.assertEqual(checkout(sku25), 152)
        self.assertEqual(checkout(sku26), 175)
        self.assertEqual(checkout(sku27), 225)
    
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
        dict5={'U':8, 'B':1}
        dict6={'U':6, 'B':1}
        dict7={'E':8, 'B':2}
        dict8={'E':8, 'B':0}
        self.assertEqual(updateCounterDict(dict1), dict2)
        self.assertEqual(updateCounterDict(dict3), dict4)
        self.assertEqual(updateCounterDict(dict5), dict6)
        self.assertEqual(updateCounterDict(dict7), dict8)

    def test_groupDiscount(self):
        array1 = [17,20,20,20,21]
        array2 = []
        array3 = [21,20,20,20,21,21,17]
        self.assertEqual(groupDiscount(array1), 82)
        self.assertEqual(groupDiscount(array2), 0)
        self.assertEqual(groupDiscount(array3), 107)

if __name__ == '__main__':
    unittest.main()

