"""Test the __iadd__ implementation requested in probelm 7."""

import unittest
from P8 import Fraction


class TestP8(unittest.TestCase):

    def test_iadd(self):
        f1 = Fraction(1,2)
        f2 = Fraction(2, 3)
        f1 += f2
        self.assertEqual(f1, Fraction(7, 6))

        f1 = Fraction(1, 3)
        f2 = Fraction(0, 5)
        f1 += f2
        self.assertEqual(f1, Fraction(1, 3))

        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f1 -= f2
        self.assertEqual(f1, Fraction(0, 1))
