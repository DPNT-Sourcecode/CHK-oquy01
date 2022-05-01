import unittest
from hello_solution import *



class TestSolution(unittest.TestCase):
    def test_hello(self):
        s1='''Hello, John!'''
        s2='''Hello, Ted!'''
        s3='''Hello, World!'''
        self.assertEqual(hello('John'), s1)
        self.assertEqual(hello('Ted'), s2)
        self.assertEqual(hello(''), s3)

if __name__ == '__main__':
    unittest.main()
