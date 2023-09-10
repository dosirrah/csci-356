"""
Test the implementation that solves 5.

5. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator
   are both integers. If either is not an integer the constructor should raise an exception.

"""

import unittest
from P5 import Fraction


class TestP5(unittest.TestCase):

    def test_instantiation(self):

        # test correct instantiations
        f = Fraction(0, 1)
        self.assertEqual(f.num, 0)
        self.assertEqual(f.den, 1)
        f = Fraction(5, 2)
        self.assertEqual(f.num, 5)
        self.assertEqual(f.den, 2)

        # test invalid instantiation in which non-integers
        # were passed to the Fraction constructor.
        try:
            r = Fraction("hello", "world")  # both invalid.
            self.assertTrue(False)  # should never reach here.
        except TypeError:
            pass

        try:
            f = Fraction(0, "hi")           # only numerator invalid
            self.assertTrue(False)  # should never reach here.
        except TypeError:
            pass

        try:
            f = Fraction("foo", 1)
            self.assertTrue(False)  # should never reach here.
        except TypeError:
            pass


