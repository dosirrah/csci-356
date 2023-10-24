"""This module provides a Python list implementation for purposes of
illustration."""

from __future__ import annotations  # allows __eq__, __add__, etc. to take Fraction as a type hint.
import numpy


class CircularBuffer:
    """
    CircularBuffer implements a doubly-ended queue with O(1) pushes and pops
    from either end.This is just for illustration purposes.
    """

    def __init__(self):
        """
        create empty circular buffer.
        """
        self._begin = 0
        self._end = 0
        self._n = 0
        self._cap = 1
        self._arr = numpy.empty(self._cap, dtype=object)

    def _grow(self, new_cap=None):
        """
        Increase capacity of the circular buffer.
        :param new_cap: capacity of the circular buffer after _grow() or double
                        the current capacity if new_cap not passed.
        :return: None
        """
        if new_cap is None:
            new_cap = self._cap * 2
        assert new_cap > self._cap
        newarr = numpy.empty(new_cap, dtype=object)

        # copy takes O(n).
        for i in range(self._n):
            j = (self._begin + i) % self._cap
            newarr[i] = self._arr[j]

        self._arr = newarr
        self._begin = 0
        self._end = self._n
        self._cap = new_cap

    def push_back(self, x: object):
        """
        Append an object to the back of the circular buffer.
        Takes amortized O(1).
        :param x: object to append
        :return: None
        """
        if self._n == self._cap-1:
            self._grow()

        self._arr[self._end] = x
        self._end = (self._end + 1) % self._cap
        self._n += 1

    def push_front(self, x: object):
        """
        Prepend an object to the circular buffer.
        Takes amortized O(1).
        :param x: object to prepend
        :return: None
        """
        if self._n == self._cap-1:
            self._grow()

        self._begin = (self._begin -1) % self._cap
        self._arr[self._begin] = x
        self._n += 1

    def pop_front(self) -> object:
        """
        Remove and return object at front of the circular buffer.
        Takes O(1).
        :return: object previously at front of the circular buffer.
        """
        if self._n == 0:
            raise IndexError
        x = self._arr[self._begin]
        self._arr[self._begin] = None
        self._begin = (self._begin + 1) % self._cap
        self._n -= 1
        return x

    def pop_back(self) -> object:
        """
        Remove and return object at back of the circular buffer.
        Takes O(1).
        :return: object previously at back of the circular buffer.
        """
        if self._n == 0:
            raise IndexError
        self._end = (self._end - 1) % self._cap
        x = self._arr[self._end]
        self._arr[self._end] = None
        self._n -= 1
        return x

    def __len__(self) -> int:
        """
        The number of objects in the circular buffer differs
        from the capacity.  Capacity refers to the amount
        of memory allocated to store objects.
        :return: number of objects in the circular buffer.
        """
        return self._n

    def capacity(self) -> int:
        """
        :return: how many objects for which memory has been alllocated.
        """
        return len(self._arr)

    def reserve(self, capacity: int):
        """
        Reserves (pre-allocates) room for objects to avoid the overhead
        of growing multiple times when you know how many objects you are
        likely to push to the front or back.

        If you plan to reserve, you may want to temporarily disable garbage
        collection while pushing to either end to avoid performing
        unnecessary mark-and-sweeps.

        :param capacity: new capacity of the circular buffer.
        :return: circular buffer with new capacity.
        """
        if capacity < self._n:
            raise ValueError("Cannot reserve less than the number of items in the buffer.")
        self._grow(capacity)

    def __getitem__(self, index: int) -> object:
        """
        Return the ith object in the circular buffer.  This does not
        remove the object.  This takes O(1) time.
        :param index: index of object to return.
        :return: object at given index.
        """
        if index >= self._n or index < -self._n:
            raise IndexError
        if index < 0:
            index = (self._end + index) % self._cap
        else:
            index = (self._begin + index) % self._cap
        return self._arr[index]

    # didn't implement __setitem__ but the implementation is similar
    # and is O(1).


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import math
    from random import randint

    N = 256

    def sweep_n(n:int) -> list:
        x = CircularBuffer()
        caps = []
        caps.append(x.capacity())
        for i in range(n):
            x.push_back(randint(0, 100000))
            caps.append(x.capacity())
        return caps

    def main():
        global N

        # For illustrative purposes, plot capacity as a function of the
        # number of objects N in the circular buffer.
        cap_list = sweep_n(N)
        plt.scatter(range(0, N+1), cap_list, color="blue")

        plt.title('Capacity vs. N')
        plt.xlabel('N')
        plt.ylabel('Capacity')

        plt.show()

        k_list = [1]
        k = 0  # number of increments
        for i in range(1, N+1):
            if cap_list[i] > cap_list[i-1]:
                k += 1
            k_list.append(k)
        plt.scatter(range(0, N+1), k_list, color="blue")

        log_list = []
        for i in range(1, N+1):
            log_list.append(1+math.log2(i))
        plt.scatter(range(0, N), log_list, color="red")

        plt.title('Number of allocatons k vs. N')
        plt.xlabel('N')
        plt.ylabel('k')

        plt.show()


    main()
