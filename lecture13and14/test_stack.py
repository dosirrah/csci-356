from stack import Stack
import unittest

class TestStack(unittest.TestCase):

    def test_instantiate(self):
        s = Stack()

    def test_push_pop(self):
        s = Stack()
        self.assertEqual(0, s.size())

        s.push(10)
        self.assertEqual(10, s.peek())
        self.assertEqual(1, s.size())

        x = s.pop()
        self.assertEqual(10, x)
        self.assertEqual(0, s.size())
