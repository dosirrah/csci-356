import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_instantiation_and_len(self):
        q = Queue()
        self.assertEqual(0, len(q))

    def test_enqueue(self):
        q = Queue()
        self.assertEqual(0, len(q))

        q.enqueue("foo")
        self.assertEqual(1, len(q))

    def test_dequeue(self):
        q = Queue()

        try:
            q.dequeue()
            self.assertFalse(True)  # should not reach here.
        except IndexError:
            pass

        q.enqueue("foo")
        item = q.dequeue()
        self.assertEqual("foo", item)

        q.enqueue("bar")
        q.enqueue("goo")
        item = q.dequeue()
        self.assertEqual("bar", item)

        item = q.dequeue()
        self.assertEqual("goo", item)




