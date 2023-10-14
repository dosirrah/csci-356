import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def test_instantiation_and_len(self):
        x = SinglyLinkedList()
        self.assertEqual(0, len(x))

    def test_push_back(self):
        x = SinglyLinkedList()

        x.push_back(10)
        self.assertEqual(1, len(x))

        x.push_back(5)
        self.assertEqual(2, len(x))

    def test_pop_front(self):
        x = SinglyLinkedList()

        try:
            x.pop_front()
            self.assertFalse(True)  # not supposed to reach here.
        except IndexError:
            pass

        x.push_back("foo")
        self.assertEqual(1, len(x))

        y = x.pop_front()
        self.assertEqual("foo", y)
        self.assertEqual(0, len(x))

        x.push_back("bar")
        x.push_back(10)
        y = x.pop_front()
        self.assertEqual("bar", y)
        self.assertEqual(1, len(x))


