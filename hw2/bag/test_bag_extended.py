# These tests are intended for grading in addition to those found
# in test_bag.  Partial credit should be given for passing those in
# test_bag.py but not those in test_bag_extended.py
import unittest
from bag import Bag

class TestBagExtended(unittest.TestCase):

    def test_add_and_in(self):
        # I have yet to add any tests here...
        b = Bag()
        self.assertEqual(0, len(b))

        b.add(5)
        self.assertEqual(1, len(b))

        self.assertTrue(5 in b)

        # add some more common case tests.
        b.add("foo")
        self.assertEqual(2, len(b))


    def test_iterator(self):

        # test iterating over empty bag.
        b = Bag()
        for _ in b:
            self.assertFalse(True)   # should not reach here.

        # test with only 1 item.
        b.add("bar")
        cnt = 0
        for x in b:
            cnt += 1
            self.assertEqual("bar", x)
        self.assertEqual(1, cnt)

        # test iterating after removal back to 0 items.
        b.remove("bar")
        self.assertEqual(0, len(b))
        for _ in b:
            self.assertFalse(True)   # should not reach here.



