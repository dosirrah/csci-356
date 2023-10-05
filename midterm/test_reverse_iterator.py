from reverse_iterator import ReverseIterator
import unittest

class TestReverseIterator(unittest.TestCase):

    def test_edge_cases(self):
        x = []
        rit = ReverseIterator(x)
        for i in rit:
            self.assertFalse(True)  # should not reach here.

        x = [1]
        rit = ReverseIterator(x)
        for i in rit:
            self.assertEqual(1, i)

    def test_iteration(self):
        x = [1, 4, 3]
        rit = ReverseIterator(x)
        y = []
        for i in rit:
            y.append(i)
        self.assertEqual([3, 4, 1], y)
