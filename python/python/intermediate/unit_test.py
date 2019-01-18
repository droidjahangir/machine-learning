import unittest
from msPack import math
from msPack import string

#Method testing

class math_test_case(unittest.TestCase):
    def test_sum(self):
        sum = math.sum(8,12)
        self.assertEqual(sum,20)

if __name__ == '__main__':
    unittest.main()


