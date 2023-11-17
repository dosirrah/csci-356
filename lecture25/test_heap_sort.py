from heap_sort import heap_sort, heap_sort_pushes
import unittest

class HeapSortTest(unittest.TestCase):

    def test_edge_cases(self):
        try:
            x = []
            heap_sort(x)
        except:
            self.assertTrue(False)  # should not raise an exception.

        x = [4]
        heap_sort(x)
        self.assertEqual(1, len(x))
        self.assertEqual(x[0], 4)

        x = [1, 5]
        heap_sort(x)
        self.assertEqual([1,5], x)

        x = [5, 1]
        heap_sort(x)
        self.assertEqual([1, 5], x)

    def test_non_edge_cases(self):

        x = [1, 9, 3, 6, 5, 11, 0]
        heap_sort(x)
        self.assertEqual([0, 1, 3, 5, 6, 9, 11], x)

    def test_heap_sort_pushes_edge_cases(self):
        x = [4]
        heap_sort_pushes(x)
        self.assertEqual(1, len(x))
        self.assertEqual(x[0], 4)

        x = [1, 5]
        heap_sort_pushes(x)
        self.assertEqual([1, 5], x)

        x = [5, 1]
        heap_sort_pushes(x)
        self.assertEqual([1, 5], x)

    def test_heap_sort_pushes_non_edge_cases(self):

        x = [1, 9, 3, 6, 5, 11, 0]
        heap_sort_pushes(x)
        self.assertEqual([0, 1, 3, 5, 6, 9, 11], x)

