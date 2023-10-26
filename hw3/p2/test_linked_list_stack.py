import unittest
from linked_list_stack import LinkedListStack


class TestLinkedListStack(unittest.TestCase):

    def test_instantiation_and_len(self):
        x = LinkedListStack()
        self.assertEqual(0, len(x))

    def test_push(self):
        x = LinkedListStack()

        x.push(10)
        self.assertEqual(1, len(x))

        x.push(5)
        self.assertEqual(2, len(x))

    def test_pop(self):
        x = LinkedListStack()

        try:
            x.pop()
            self.assertFalse(True)  # not supposed to reach here.
        except IndexError:
            pass

        x.push("foo")
        self.assertEqual(1, len(x))

        y = x.pop()
        self.assertEqual("foo", y)
        self.assertEqual(0, len(x))

    def test_peek(self):
        x = LinkedListStack()
        try:
            x.peek()
            self.assertTrue(False)  # should not reach here.
        except IndexError:
            pass

        x.push("blah")
        self.assertEqual(1, len(x))
        self.assertEqual("blah", x.peek())
        self.assertEqual(1, len(x))  # peek shouldn't change length.
