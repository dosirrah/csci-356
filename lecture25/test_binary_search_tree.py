from binary_search_tree import BinarySearchTree
import unittest

class TestBST(unittest.TestCase):

    def test_edge_cases(self):
        t = BinarySearchTree()
        self.assertEqual(0, len(t))

        t.put(5, "foo")
        self.assertEqual(1, len(t))

    def test_find(self):
        t = BinarySearchTree()

        try:
            t.find(5)
            self.assertTrue(False)  # should not reach here.
        except KeyError:
            pass

        t.put(12, "goo")
        t.put(1, "bar")
        self.assertEqual(2, len(t))
        v = t.find(12)
        self.assertEqual("goo", v)
        v = t.find(1)
        self.assertEqual("bar", v)

        try:
            t.find(1231)
            self.assertFalse(True)  # should not reach here.
        except KeyError:
            pass
