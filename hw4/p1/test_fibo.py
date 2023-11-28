import unittest
from hw4.p1.fibo import fibo_recurse, fibo_iterative

class TestFibonacciRecursive(unittest.TestCase):
    def test_edge_cases(self):
        try:
            fibo_iterative(-1)
        except ValueError:
            pass

        self.assertEqual([0], fibo_recurse(0))
        self.assertEqual([0, 1], fibo_recurse(1))
        self.assertEqual([0, 1, 1], fibo_recurse(2))

    def test_common_cases(self):
        self.assertEqual([0, 1, 1, 2, 3, 5], fibo_recurse(5))
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21], fibo_recurse(8))


class TestFibonacciIterative(unittest.TestCase):

    def test_edge_cases(self):

        try:
            fibo_iterative(-1)
        except ValueError:
            pass

        self.assertEqual([0], fibo_iterative(0))
        self.assertEqual([0, 1], fibo_iterative(1))
        self.assertEqual([0, 1, 1], fibo_iterative(2))

    def test_common_cases(self):
        self.assertEqual([0, 1, 1, 2, 3, 5], fibo_iterative(5))
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21], fibo_iterative(8))

