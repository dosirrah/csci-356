import unittest
from P6 import Fraction


class TestP6(unittest.TestCase):

    def test_instantiation(self):
        f = Fraction(1, 2)
        self.assertEqual(f.num, 1)
        self.assertEqual(f.den, 2)

        f = Fraction(-1, 2)
        self.assertEqual(f.num, -1)
        self.assertEqual(f.den, 2)

        f = Fraction(1, -2)
        self.assertEqual(f.num, -1)
        self.assertEqual(f.den, 2)

    def test_lt(self):
        self.assertLess(Fraction(-1, 2), Fraction(-1, 3))
        self.assertLess(Fraction(1, -2), Fraction(-1, 3))
        self.assertLess(Fraction(1, -2), Fraction(1, -3))

    def test_ge(self):
        self.assertGreaterEqual(Fraction(-1, 3), Fraction(-1, 2))  # one denominator negative
        self.assertGreaterEqual(Fraction(-1, 3), Fraction(1, -2))  # both denominators negatvie
        self.assertGreaterEqual(Fraction(1, -3), Fraction(1, -2))  # both denominators negative
        self.assertTrue(Fraction(9, 2) >= Fraction(-18, -4))       # double negative
        self.assertFalse(Fraction(8, -2) >= Fraction(1, 2))        # countercase

    def test_ne(self):
        self.assertNotEqual(Fraction(-1, 3), Fraction(-1, 2))
        self.assertFalse(Fraction(0, -1) != Fraction(0, 3))
        self.assertFalse(Fraction(-1, 2) != Fraction(1, -2))
        self.assertFalse(Fraction(-1, -2) != Fraction(1, 2))

