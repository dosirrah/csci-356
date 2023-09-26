"""
**Problem 6**: (2 points) Write a program that verifies that the list
index operator is O(1).  The program must plot the run time of the
list index operator as a function of n using matplotlib.
"""

import matplotlib.pyplot as plt
from random import randint
import time
import sys


N = 1000
M = 10


def perf_test_list_index(x:list, m:int):
    """

    :param x: perform list operations on x.
    :param m: do it m times.
    :return:
    """
    n = len(x)
    for _ in range(m):
        _ = x[randint(0, n-1)]   # randint returns values in [0,n-1] including n-1.


def main():

    run_time_list = []
    for n in range(1, N+1):
        x = [randint(0,100000) for i in range(n)]
        start_time_secs = time.time()
        perf_test_list_index(x, M)
        end_time_secs = time.time()
        elapsed_secs = end_time_secs - start_time_secs
        run_time_list.append(elapsed_secs / M)
        if n % 100 == 0:
            print("n=%d" % n)
            sys.stdout.flush()

    plt.scatter(range(1, N+1), run_time_list, color="blue")

    plt.title('Execution time of an index operation vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

main()

