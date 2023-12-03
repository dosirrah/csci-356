from heapq import heapify, heappop
from random import randint
from bisect import bisect_left
import numpy as np
# from lecture15to17.list_queue import ListQueue
# from lecture15to17.sll_queue import SLLQueue


def problem2():

    # 2(a)
    x = []
    x.append(5)

    # 2(b)
    n = 1000
    x = []
    for i in range(n):
        x.append(i)

    # 2(c)
    x = [randint(0, 1000) for x in range(n)]


    # 2(g)
    n = 10000
    k = 100

    x = []
    i = 0
    for _ in range(n):
        i += randint(0, 10)
        x.append(i)

    print(f"inserted {n} items into list x in increasing order.  Max value is {i}.")
    found = 0
    for _ in range(k):
        y = randint(0, i)
        j = bisect_left(x, y)
        if j < len(x) and x[j] == y:
            found += 1

    # it is expected that found should be roughly k/5 since the numbers
    # in the list are on average 5 apart from each other..
    print(f"out of {k} random searches we found {found} values.")


def problem3a():
    n = 100
    d = {}
    for i in range(n):
        j = randint(0, len(d))
        d[i] = j


def problem3b():
    m = 100
    n = 1000
    kv = [(randint(0, 10000), randint(0, 10000)) for _ in range(n)]
    d = dict(kv)
    x = 0
    for i in range(m):
        i = randint(0, n - 1)
        x += d[kv[i][0]]


def problem3c():
    k = 0
    kv = []
    for _ in range(n):
        k += randint(0, 10)
        v = randint(0, 100000)
        kv.append((k, v))
    d = dict(kv)
    for i in range(m):
        k, v = kv.pop()
        del d[k]

def problem6_factorial(n):
    if n < 0:
        raise Error("n must be nonnegative")
    if n ==1 or n == 0:
        return 1
    return n * problem6_factorial(n-1)


def problem7(x: list) -> list:
    n = len(x)
    result = [None]*n
    cnts = [0] * 101
    for i in x:
        cnts[i] += 1

    k = 0
    for j in range(101):
        while cnts[j] > 0:
            result[k] = j
            k += 1
            cnts[j] -= 1
    return list(result)


def problem9a(x: list, k:int) -> int:
    """Write a function to find the the $k$th
    smallest value using python's \verb|sorted|.  What is its
    time complexity as a function of $n$ and $k$"""

    return sorted(x)[k]


def problem9b(x: list, k: int) -> int:
    """find the $k$th smallest value using a binary
       min heap. k uses the convention of starting
       from 0.  Therefore k=0 refers to the smallest."""
    if k < 0:
        raise IndexError("k must be nonnegative.")
    if len(x) == 0:
        raise ValueError("x must be a non-zero length list.")
    heapify(x)
    y = None
    for i in range(k+1):
        y = heappop(x)
    return y
