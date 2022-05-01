import unittest
from hello_solution import *



class TestSolution(unittest.TestCase):
    def test_hello(self):
        s1='''Hello John'''
        self.assertEqual(hello('John'), s1)

if __name__ == '__main__':
    unittest.main()