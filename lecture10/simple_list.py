"""This module provides a Python list implementation for purposes of
illustration."""


import numpy


class SimpleList:
    """SimpleList implements a subset of the Python lists functionality but in Python
    rather than C++.  This is just for illustration purposes. SimpleList
    implements a dynamic array that supports amortized O(1) append."""

    def __init__(self):
        self._n = 0
        self._cap = 1
        self._arr = numpy.empty(self._cap, dtype=object)

    def append(self, x: object):
        if self._n == self._cap:
            self._cap *= 2
            newarr = numpy.empty(self._cap, dtype=object)

            # copy takes O(n).
            for i in range(self._n):
                newarr[i] = self._arr[i]

            self._arr = newarr

        self._arr[self._n] = x
        self._n += 1

    def __setitem__(self, i: int, value):
        self._arr[i] = value


    def __getitem__(self, i: int) -> object:
        return self._arr[i]

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
        x = SimpleList()
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
