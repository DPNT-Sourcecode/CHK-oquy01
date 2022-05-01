import unittest
from sum_solution import *



class TestSolution(unittest.TestCase):
    def test_compute(self):
        self.assertEqual(compute(1,2), 3)
        self.assertEqual(compute(2,3), 5)
        self.assertEqual(compute(0,100), 100)

if __name__ == '__main__':
    unittest.main()