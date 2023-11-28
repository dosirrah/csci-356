from lecture26.binary_search_tree_set import BinarySearchTreeSet
import unittest


class TestBST(unittest.TestCase):

    def test_edge_cases(self):
        t = BinarySearchTreeSet()
        self.assertEqual(0, len(t))

        t.add(5)
        self.assertEqual(1, len(t))

    def test_in(self):
        t = BinarySearchTreeSet()

        self.assertFalse(5 in t)

        t.add(12)
        t.add(1)
        self.assertEqual(2, len(t))
        self.assertTrue(12 in t)
        self.assertTrue(1 in t)
        self.assertFalse(7 in t)  # test in between
        self.assertFalse(0 in t)  # test below lowest
        self.assertFalse(15 in t) # test above highest
