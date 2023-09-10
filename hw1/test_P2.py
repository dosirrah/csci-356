
import unittest
from P2 import Fraction


class TestP2(unittest.TestCase):

    def test_p2_instantiation(self):
        """Tests instnantiation of the Fraction class."""

        print("Running test")
        f = Fraction(1, 2)
        self.assertEqual(f.num, 1)
        self.assertEqual(f.den, 2)

        # # I am intentionally keeping the next line because it can demonstrate what happens
        # # when a test fails.
        # assert f.num == 3  # Uncomment if you want to see what happens when a test fails.

        f = Fraction(3, 9)
        self.assertEqual(f.num, 1)  # doesn't reduce the fraction at instantiation.
        self.assertEqual(f.den, 3)

        f = Fraction(9, 12)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.den, 4)

    def test_add(self):

        # The add() function should still work even though reductoin takes place
        # in __init__ rather than in add().

        f1 = Fraction(0, 1)
        f2 = Fraction(1, 2)
        self.assertEqual(f1 + f2, f2)

        f3 = Fraction(2, 3)
        f4 = f2 + f3
        self.assertEqual(f4, Fraction(7, 6), str(f4))
