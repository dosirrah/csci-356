

import unittest
from P3 import Fraction


class TestP3(unittest.TestCase):

    def test_sub(self):
        f = Fraction(1,2) - Fraction(1,2)
        self.assertEqual(f.num, 0)
        self.assertEqual(f.den, 1)
        self.assertEqual(f, Fraction(0, 1))  # Note: 0/1 == 0.

        f = Fraction(4,3) - Fraction(1,2)
        self.assertEqual(f, Fraction(5, 6))

        f = Fraction(1, 5) - Fraction(7, 10)
        self.assertEqual(f, Fraction(-1, 2))

    def test_mul(self):

        f = Fraction(3, 8) * Fraction(7,4)   # test typical case.
        self.assertEqual(f, Fraction(21, 32))
        f = Fraction(0,1 ) * Fraction(0, 1)  # test 0 * 0.
        self.assertEqual(f, Fraction(0, 1))

        f = Fraction(0,1) * Fraction(4, 3)   # test 0 * something
        self.assertEqual(f, Fraction(0, 1), str(f))

        f = Fraction(4, 3) * Fraction(0, 1)  # test commutativity with 0.
        self.assertEqual(f, Fraction(0, 1), str(f))

        f = Fraction(4, 3) * Fraction(3, 4)  # test a * 1 / a == 1.
        self.assertEqual(f, Fraction(1, 1), str(f))

    def test_truediv(self):
        f = Fraction(4, 5) / Fraction(2, 7)  # typical case
        self.assertEqual(f, Fraction(14, 5))

        f = Fraction(3, 4) / Fraction(3, 4)  # test dividing a nubmer by itself.
        self.assertEqual(f, Fraction(1, 1))



