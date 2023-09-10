"""
Testing relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)

"""

import unittest

import unittest
from P4 import Fraction


class TestP4(unittest.TestCase):

    def test_gt(self):
        self.assertGreater(Fraction(3,2), Fraction(2,3))
        self.assertTrue(Fraction(3,2) > Fraction(2,3))
        self.assertFalse(Fraction(2,3) > Fraction(3,4))
        self.assertFalse(Fraction(1,2) > Fraction(1,2))
        self.assertFalse(Fraction(0,9) > Fraction(1,99))
        self.assertTrue(Fraction(1,99) > Fraction(0,9))
        self.assertFalse(Fraction(0,1) > Fraction(4, 19))

    def test_ge(self):
        self.assertGreaterEqual(Fraction(5,3), Fraction(1, 2))  # typical 5/3 >= 1/2
        self.assertGreaterEqual(Fraction(1,2), Fraction(1,2))   # 1/2 >= 1/2
        self.assertFalse(Fraction(5, 4) >= Fraction(3, 2))      # 5/4 >= 3/2 is False
        self.assertTrue(Fraction(0, 1) >= Fraction(-1, 1))          # 0 >= -1
        self.assertTrue(Fraction(-1, 1) >= Fraction(-2, 1))              # -1 >= -2
        self.assertTrue(Fraction(-1, 1) >= Fraction(-2, 2))              # -1 >= -1
        self.assertTrue(Fraction(0, 1) >= Fraction(0, 1))       # 0 >= 0

    def test_lt(self):
        self.assertLess(Fraction(1, 2), Fraction(2, 1))  # 1/2 < 2
        self.assertLess(Fraction(5, 4), Fraction(3,2))   # 5/4 < 3/2
        self.assertFalse(Fraction(3, 2) < Fraction(5, 4))
        self.assertTrue(Fraction(-1, 1) < Fraction(0, 1))
        self.assertTrue(Fraction(-2, 1) < Fraction(-1, 1))
        self.assertFalse(Fraction(-2, 2) < Fraction(-1, 1))

    def test_le(self):
        self.assertLessEqual(Fraction(1, 2), Fraction(2, 1))  # 1/2 < 2
        self.assertLessEqual(Fraction(5, 4), Fraction(3,2))   # 5/4 < 3/2
        self.assertFalse(Fraction(3, 2) <= Fraction(5, 4))
        self.assertTrue(Fraction(-1, 1) <= Fraction(0, 1))
        self.assertTrue(Fraction(-2, 1) <= Fraction(-1, 1))
        self.assertTrue(Fraction(-2, 2) <= Fraction(-1, 1))

    def test_ne(self):
        self.assertNotEqual(Fraction(1, 2), Fraction(2, 1))  # 1/2 != 2
        self.assertNotEqual(Fraction(5, 4), Fraction(3,2))   # 5/4 != 3/2
        self.assertTrue(Fraction(-1, 1) != Fraction(0, 1))
        self.assertTrue(Fraction(-2, 1) != Fraction(-1, 1))
        self.assertFalse(Fraction(-2, 2) != Fraction(-1, 1))

