import unittest
from circular_buffer import CircularBuffer


class TestCircularBuffer(unittest.TestCase):
    def test_instantiate_and_len(self):
        cbuf = CircularBuffer()

        self.assertEqual(0, len(cbuf))

    def test_push_back_pop_front(self):
        cbuf = CircularBuffer()

        try:
            cbuf.pop_front()
            self.assertFalse(True)  # should not reach here.
        except IndexError:
            pass   # supposed to go here.

        cbuf.push_back(10)
        self.assertEqual(1, len(cbuf))

        x = cbuf.pop_front()
        self.assertEqual(10, x)
        self.assertEqual(0,len(cbuf))


    def test_rotating_push_back_pop_fronts(self):
        cbuf = CircularBuffer()
        for i in range(10):
            cbuf.push_back(i)  # grows the buffer a bit.

        for i in range(5):
            j = cbuf.pop_front()
            self.assertEqual(i, j)

        cap_before = cbuf.capacity()
        self.assertLessEqual(10, cap_before)

        for i in range(10, 100):
            cbuf.push_back(i)
            j = cbuf.pop_front()
            self.assertEqual(j, i-5)
            self.assertEqual(5, len(cbuf))

        # even though we added many to the circular buffer,
        # we were also removing items at the same rate, so the
        # capacity should not have increased.
        self.assertEqual(cap_before, cbuf.capacity())

    def test_push_front_pop_back(self):
        cbuf = CircularBuffer()

        try:
            cbuf.pop_back()
            self.assertFalse(True)  # should not reach here.
        except IndexError:
            pass   # supposed to go here.

        cbuf.push_front(10)
        self.assertEqual(1, len(cbuf))

        x = cbuf.pop_back()
        self.assertEqual(10, x)
        self.assertEqual(0,len(cbuf))

    def test_rotating_push_front_pop_backs(self):
        cbuf = CircularBuffer()
        for i in range(10):
            cbuf.push_front(i)  # grows the buffer a bit.

        for i in range(5):
            j = cbuf.pop_back()
            self.assertEqual(i, j)

        cap_before = cbuf.capacity()
        self.assertLessEqual(10, cap_before)

        for i in range(10, 100):
            cbuf.push_front(i)
            j = cbuf.pop_back()
            self.assertEqual(j, i-5)
            self.assertEqual(5, len(cbuf))

        # even though we added many to the circular buffer,
        # we were also removing items at the same rate, so the
        # capacity should not have increased.
        self.assertEqual(cap_before, cbuf.capacity())


    def test_many_push_backs(self):
        pass