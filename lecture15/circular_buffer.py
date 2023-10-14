"""This module provides a Python list implementation for purposes of
illustration."""


import numpy


class CircularBuffer:
    """
    CircularBuffer implements a doubly-ended queue with O(1) pushes and pops
    from either end.This is just for illustration purposes.
    """

    def __init__(self):
        self._begin = 0
        self._end = 0
        self._n = 0
        self._cap = 1
        self._arr = numpy.empty(self._cap, dtype=object)

    def _grow(self):
        new_cap = self._cap * 2
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
        if self._n == self._cap:
            self._grow()

        self._arr[self._end] = x
        self._end = (self._end + 1) % self._cap
        self._n += 1

    def push_front(self, x: object):
        if self._n == self._cap:
            self._grow()

        self._begin = (self._begin -1) % self._cap
        self._arr[self._begin] = x
        self._n += 1

    def pop_front(self) -> object:
        if self._n == 0:
            raise IndexError
        x = self._arr[self._begin]
        self._arr[self._begin] = None
        self._begin = (self._begin + 1) % self._cap
        self._n -= 1
        return x

    def pop_back(self) -> object:
        if self._n == 0:
            raise IndexError
        self._end = (self._end - 1) % self._cap
        x = self._arr[self._end]
        self._arr[self._end] = None
        self._n -= 1
        return x

    def __len__(self) -> int:
        return self._n

    def capacity(self) -> int:
        return len(self._arr)


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
            x.append(randint(0, 100000))
            caps.append(x.capacity())
        return caps

    def main():
        global N

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
