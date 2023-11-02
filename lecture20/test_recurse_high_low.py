import unittest
from recurse_high_low import recurse_high_low

class TestRecurseHighLow(unittest.TestCase):

    def test_empty(self):
        lst = []
        i = recurse_high_low(lst, 3)
        self.assertIsNone(i)

    def test_miss(self):
        lst = [5]
        # search high
        i = recurse_high_low(lst, 6)
        self.assertIsNone(i)
        # search low
        i = recurse_high_low(lst, 3)
        self.assertIsNone(i)

        lst = [12,16]

        # search high
        i = recurse_high_low(lst, 19)
        self.assertIsNone(i)

        # search low
        i = recurse_high_low(lst, 6)
        self.assertIsNone(i)

        # search middle
        i = recurse_high_low(lst, 15)
        self.assertIsNone(i)

    def test_hit(self):
        lst = [4]
        i = recurse_high_low(lst, 4)
        self.assertEqual(0, i)

        lst = [3, 9]
        i = recurse_high_low(lst, 9)
        self.assertEqual(1, i)
        i = recurse_high_low(lst, 3)
        self.assertEqual(0, i)