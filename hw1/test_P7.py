"""Test the __radd__ implementation requested in probelm 7."""

import unittest
from P7 import Fraction


class TestP7(unittest.TestCase):

    def test_instantiation(self):
        f = Fraction(1, 2)

    def test_radd(self):
        f = 5 + Fraction(1, 2)
        self.assertEqual(f.den, 2)
        self.assertEqual(f.num, 11)

        try:
            f = "foo" + Fraction(1, 2)
            self.assertTrue(False)    # should not reach here.
        except TypeError:
            pass    # exception was intentionally raised to verify error handling.

        f = Fraction(1, 2) + 5
        self.assertEqual(f.den, 2)
        self.assertEqual(f.num, 11)

