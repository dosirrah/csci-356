import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_instantiation_and_len(self):
        x = LinkedList()
        self.assertEqual(0, len(x))

    def test_push_back(self):
        x = LinkedList()

        x.push_back(10)
        self.assertEqual(1, len(x))

        x.push_back(5)
        self.assertEqual(2, len(x))

    def test_pop_back(self):
        x = LinkedList()

        try:
            x.pop_back()
            self.assertFalse(True)  # not supposed to reach here.
        except IndexError:
            pass

        x.push_back("foo")
        self.assertEqual(1, len(x))

        y = x.pop_back()
        self.assertEqual("foo", y)
        self.assertEqual(0, len(x))


    def test_push_front(self):
        x = LinkedList()

        x.push_front(10)
        self.assertEqual(1, len(x))

        x.push_front(5)
        self.assertEqual(2, len(x))

    def test_pop_front(self):
        x = LinkedList()

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


    def test_iteration(self):

        x = LinkedList()
        for i in x:
            self.assertTrue(False)  # should not reach here.

        x.push_back("foo")
        for i in x:
            self.assertEqual("foo", i)

        x.push_back("bar")
        it = iter(x)
        i = next(it)
        self.assertEqual("foo", i)

        i = next(it)
        self.assertEqual("bar", i)

        try:
            next(it)
            self.assertFalse(True)  # should not reach here.
        except StopIteration:
            pass


