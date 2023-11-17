import unittest
from min_heap import MinHeap

class TestMinHeap(unittest.TestCase):

    def test_empty(self):
        h = MinHeap()
        try:
            _ = h.pop()
            self.assertFalse(True)  # should not reach here.
        except IndexError:
            pass   # exception should be raised when popping an empty heap.

    def test_push_pop(self):
        h = MinHeap()
        h.push(5)
        self.assertEqual(len(h), 1)
        x = h.pop()
        self.assertEqual(len(h), 0)
        self.assertEqual(x, 5)

    def test_multiple_pushes_and_pops(self):
        h = MinHeap()
        h.push(12)
        h.push(5)
        h.push(15)

        # should be
        #   5
        #  / \
        # 12 15
        self.assertEqual(len(h), 3)
        x = h.pop()
        self.assertEqual(x, 5)
        x = h.pop()
        self.assertEqual(x, 12)
        x = h.pop()
        self.assertEqual(x, 15)
        self.assertEqual(len(h), 0)
        try:
            _ = h.pop()
            self.assertFalse(True)  # should not reach here.
        except IndexError:
            pass  # expected an IndexError when attempting to pop an empty heap.

    def test_make_heap(self):
        h = MinHeap()
        x = []

        h.make_heap(x)
        self.assertEqual(0, len(h))

        x = [4]
        h.make_heap(x)  # make_heap modifies and adopts x.
        self.assertEqual(1, len(h))
        self.assertEqual(2, len(x))
        self.assertEqual(4, x[1])
        y = h.pop()
        self.assertEqual(4, y)

        x = [4, 2]
        h.make_heap(x)
        self.assertEqual(3, len(x))
        self.assertEqual([0, 2, 4], x)
        self.assertEqual(2, h.pop())
        self.assertEqual(1, len(h))
        self.assertEqual(4, h.pop())
        self.assertEqual(0, len(h))

        x = [4, 2, 5]
        h.make_heap(x)
        self.assertEqual(4, len(x))
        self.assertEqual(0, x[0])
        self.assertEqual(2, x[1])
        self.assertEqual(2, h.pop())
        self.assertEqual(4, h.pop())
        self.assertEqual(5, h.pop())
        self.assertEqual(0, len(h))

