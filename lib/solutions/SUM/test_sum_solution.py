import unittest
from sum_solution import *

class TestSolution(unittest.TestCase):
    def test_compute(self):
        self.assertEqual(compute(1,2), 3)


if __name__ == '__main__':
    unittest.main()