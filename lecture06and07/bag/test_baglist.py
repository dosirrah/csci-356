
import unittest

from baglist import BagList

class TestBagList(unittest.TestCase):

    def test_instantiation_and_len(self):
        b = BagList()
        self.assertEqual(0, len(b))

        b = BagList([1,5,4])
        self.assertEqual(3, len(b))

        b = BagList([])
        self.assertEqual(0, len(b))

    def test_add_in_and_count(self):
        b = BagList()
        self.assertEqual(0, b.count("foo"))
        self.assertFalse("foo" in b)

        b.add("foo")
        self.assertTrue("foo" in b)

        self.assertEqual(1, b.count("foo"))

        b.add("foo")
        self.assertTrue("foo" in b)
        self.assertEqual(2, b.count("foo"))

        b.add("bar")
        self.assertEqual(1, b.count("bar"))

    def test_remove(self):
        b = BagList([])
        try:
            b.remove(1)
            self.assertTrue(False)  # should not reach here.
        except KeyError:
            pass

        b = BagList([5,3])
        self.assertTrue(5 in b)
        self.assertTrue(3 in b)
        self.assertEqual(2, len(b))

        b.remove(3)
        self.assertFalse(3 in b)
        self.assertTrue(5 in b)
        self.assertEqual(1, len(b))

    def test_discard(self):
        b = BagList()
        b.discard(6)  # shouldn't raise an exception.
        b.add(6)
        self.assertTrue(6 in b)
        b.discard(6)
        self.assertFalse(6 in b)

        b = BagList(["foo", 5, 5, 8, "bar"])
        self.assertEqual(2, b.count(5))
        self.assertTrue("foo" in b)
        self.assertTrue("bar" in b)
        b.discard(5)
        self.assertEqual(1, b.count(5))
        b.discard(5)
        self.assertEqual(0, b.count(5))
        self.assertTrue(5 not in b)

    def test_removeall(self):
        b = BagList()
        try:
            b.removeall(5)
            self.assertTrue(False)  # should not reach here
        except KeyError:
            pass

        b = BagList([5, 6, "foo", 8, "foo", "foo", 3])
        self.assertEqual(3, b.count("foo"))
        self.assertEqual(7, len(b))
        b.removeall("foo")
        self.assertEqual(0, b.count("foo"))
        self.assertEqual(4, len(b))


    def test_discardall(self):
        b = BagList()
        b.discardall(5)   # should not raise an exception.

        b = BagList([5, 6, "foo", 8, "foo", "foo", 3])
        self.assertEqual(3, b.count("foo"))
        self.assertEqual(7, len(b))
        b.discardall("foo")
        self.assertEqual(0, b.count("foo"))
        self.assertEqual(4, len(b))


