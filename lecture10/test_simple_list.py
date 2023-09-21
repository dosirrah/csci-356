"""SimpleList implements a subset of the Python lists functionality but in Python
rather than C++.  This is just for illustration purposes. SimpleList
implements a dynamic array that supports amortized O(1) append."""
import unittest
from simple_list import SimpleList

class TestSimpleList(unittest.TestCase):

    def test_instantiation_and_len(self):

        x = SimpleList()
        self.assertEqual(0, len(x))
        self.assertEqual(1, x.capacity())

    def test_append_and_getitem(self):
        x = SimpleList()
        x.append(2)
        self.assertEqual(1, len(x))
        self.assertEqual(1, x.capacity())
        self.assertEqual(2, x[0])

        x.append(23)
        self.assertEqual(2, len(x))
        self.assertEqual(2, x.capacity())
        self.assertEqual(2, x[0])
        self.assertEqual(23, x[1])

        x.append(11)
        self.assertEqual(3, len(x))
        self.assertEqual(4, x.capacity())
        self.assertEqual(11, x[2])

        x.append(55)
        self.assertEqual(4, len(x))
        self.assertEqual(4, x.capacity())

        x.append(-33)
        self.assertEqual(5, len(x))
        self.assertEqual(8, x.capacity())

