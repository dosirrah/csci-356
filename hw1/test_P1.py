from P1 import Fraction, gcd
import unittest

class TestP1(unittest.TestCase):

    def test_p1_instantiation(self):
        """Tests instnantiation of the Fraction class."""

        print("Running test")
        f = Fraction(1, 2)
        self.assertEqual(f.num, 1)
        self.assertEqual(f.den, 2)

        # # I am intentionally keeping the next line because it can demonstrate what happens
        # # when a test fails.
        # assert f.num == 3  # Uncomment if you want to see what happens when a test fails.

        f = Fraction(3, 9)
        self.assertEqual(f.num, 3)  # doesn't reduce the fraction at instantiation.
        self.assertEqual(f.den, 9)

    def test_p1_accessor_methods(self):
        """Tests use of the getNum and getDen accessor function."""
        f = Fraction(1, 2)
        self.assertEqual(f.getNum(), 1)
        self.assertEqual(f.getDen(), 2)

    def test_gcd(self):
        self.assertEqual(5, gcd(5, 10))
        self.assertEqual(30, gcd(60,90))

        self.assertEqual(5, gcd(0, 5))

        # # The implementation of gcd() in the book doesn't handle the next
        # # case.  Obviously the authors didn't do enough unit testing.
        # # I modified gcd so that it will handle this case and so that it
        # # provides a more meaningful error when both arguments are 0.
        # # I commented the next line, because I'm not going to penalize students
        # # for a limitation (error?) in the book.
        self.assertEqual(5, gcd(5, 0))

        self.assertEqual(1, gcd(-5, 1))

        # The implementation of gcd() in the book also fails on the next one.  It returns -1.
        self.assertEqual(1, gcd(5, -1))

    def test_add(self):
        f1 = Fraction(0, 1)
        f2 = Fraction(1, 2)
        self.assertEqual(f1 + f2, f2)

        f3 = Fraction(2, 3)
        f4 = f2 + f3
        self.assertEqual(f4, Fraction(7, 6), str(f4))

    def test_eq(self):
        f1 = Fraction(2, 4)
        f2 = Fraction(1, 2)
        self.assertEqual(f1, f2)   # Calls the equal operators, i.e., f == f2.

        f3 = Fraction(3, 7)
        self.assertNotEqual(f1, f3)
        self.assertNotEqual(f2, f3)

    def test_str(self):
        s = str(Fraction(1, 2))
        self.assertEqual(s, "1/2")

        s = str(Fraction(2, 4))
        self.assertEqual(s, "2/4")  # no reduction in __init__.
