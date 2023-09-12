# As an example of Test-Driven Development (TDD), I started writing tests write
# after deciding on a basic programming interface to the Bag class.
# I will flesh out Bag.py as I add tests.  This will do this
# in class on Thursday, September 7.

import unittest
from bag import Bag

class TestBag(unittest.TestCase):

    def test_instantiation_and_len(self):
        b = Bag()
        self.assertEqual(0, len(b))

        b = Bag([1,5,6])
        self.assertEqual(3, len(b))

    def test_add_and_in(self):
        # I have yet to add any tests here...
        b = Bag()
        self.assertEqual(0, len(b))

        b.add(5)
        self.assertEqual(1, len(b))

        self.assertTrue(5 in b)

        # add some more common case tests.

    def test_remove(self):
        b = Bag()
        try:
            b.remove(5)
            # should never get here.
            self.assertFalse(True)
        except KeyError:
            pass

        b = Bag([1])
        b.remove(1)
        self.assertFalse(1 in b)
        self.assertEqual(0, len(b))

        b = Bag([1,5,6])
        b.remove(5)
        self.assertFalse(5 in b)
        self.assertEqual(2, len(b))

    def test_count(self):
        b = Bag()
        self.assertEqual(0, b.count("foo"))

        b.add(12)
        self.assertEqual(1, b.count(12))

        b.add("hello")
        self.assertEqual(1, b.count("hello"))

        b.add("hello")
        self.assertEqual(2, b.count("hello"))
        self.assertEqual(1, b.count(12))
