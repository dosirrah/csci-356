import unittest
from hw5 import problem2, problem3a, problem3b
from hw5 import problem6_factorial, problem7, problem9b

class TestHW5(unittest.TestCase):

    def test_problem2(self):
        problem2()   # only testing if it raises an exception

    def test_problem3(self):
        problem3a()  # only testing if it raises an exception
        problem3b()

    def test_problem6_factorial(self):
        self.assertEqual(1, problem6_factorial(0))
        self.assertEqual(1, problem6_factorial(1))
        self.assertEqual(2, problem6_factorial(2))
        self.assertEqual(6, problem6_factorial(3))
        self.assertEqual(24, problem6_factorial(4))

    def test_problem7(self):
        self.assertEqual([1], problem7([1]))
        self.assertEqual([2, 5], problem7([5, 2]))
        self.assertEqual([6, 7, 9], problem7([6, 9, 7]))
        self.assertEqual([1, 2, 5, 19, 23, 66],
                          problem7([23, 2, 19, 5, 1, 66]))

    def test_problem9b(self):
        x = [1]
        self.assertEqual(1, problem9b([1], 0))

        x = [4, 1, 9]
        self.assertEqual(1, problem9b(x, 0))
        x = [4, 1, 9]
        self.assertEqual(4, problem9b(x, 1))
        x = [4, 1, 9]
        self.assertEqual(9, problem9b(x, 2))

