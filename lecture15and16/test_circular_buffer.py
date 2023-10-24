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
        cbuf = CircularBuffer()
        for i in range(100):
            cbuf.push_back(i)  # grows the buffer a bit.

        self.assertEqual(100, len(cbuf))
        self.assertEqual(99, cbuf.pop_back())
        self.assertEqual(0, cbuf.pop_front())

    def test_reserve(self):
        cbuf = CircularBuffer()
        cbuf.reserve(10)
        self.assertEqual(10, cbuf.capacity())

        # verify that no capacity changes occur while there is
        # reserved room.
        for i in range(9):
            cbuf.push_back(i)
            self.assertEqual(10, cbuf.capacity())

        # force it to grow once reserved capacity has been exhausted.
        cbuf.push_back("foo")
        self.assertEqual(20, cbuf.capacity())

    def test_getitem(self):
        cbuf = CircularBuffer()
        try:
            _ = cbuf[0]
            # should never reach here.
            self.assertFalse(True)
        except IndexError:
            pass

        try:
            _ = cbuf[-1]
            # should never reach here.
            self.assertFalse(True)
        except IndexError:
            pass

        cbuf.push_back("foo")
        self.assertEqual("foo", cbuf[0])
        self.assertEqual("foo", cbuf[-1])
        try:
            _ = cbuf[1]
            # should never each here.
            self.assertFalse(True)
        except IndexError:
            pass

        cbuf.push_back("bar")
        self.assertEqual("foo", cbuf[0])
        self.assertEqual("bar", cbuf[1])
        self.assertEqual("bar", cbuf[-1])
        self.assertEqual("foo", cbuf[-2])

        try:
            _ = cbuf[-3]
            # should never each here.
            self.assertFalse(True)
        except IndexError:
            pass

        x = cbuf.pop_front()
        self.assertEqual("foo", x)
        cbuf.push_back("blah")
        self.assertEqual("bar", cbuf[0])
        self.assertEqual("blah", cbuf[1])
