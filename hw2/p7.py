"""
**Problem 7**: (2 points) Write a program that compares the performance of the
`del` operator on lists and dictionaries.  The main program should plot
the run time of each on the same plot as a function of n.  Also plot
functions that bound the time complexity and print out what you think
is the time complexity of `del` operators for lists and dictionaries
using big-O notation.  When measuring performance on the list `del`
operator, be sure to delete items at random locations from the list.
"""

import matplotlib.pyplot as plt
from random import randint, shuffle
import sys
import time

N = 100000
M = 100
SKIP = 5000


def sweep_n_for_lists(n: int, m:int, skip:int) -> list:
    """
    sweep the length of the lists while measuring the performance
    of the delete operator.

    :param n: sweep list lengths from 1 to n.
    :param m: repeat each test m times to average execution time.
    :param skip: number of values for n to skip with each measurement.
    :return:
    """

    run_time_list = []

    # we use m lists so that we can remove 1 item from each of the
    # m lists and measure the time elapsed across all m deletions
    # and divide by m to get an average.
    lists = [list() for _ in range(m)]
    iteration = 0

    for j in range(1, n, skip):
        iteration += 1
        for x in lists:
            while len(x) < j:
                x.append(randint(0, 10000))

        start_time_secs = time.time()
        for x in lists:
            del x[randint(0, len(x)-1)]
        end_time_secs = time.time()

        elapsed_secs = end_time_secs - start_time_secs
        run_time_list.append(elapsed_secs / m)

        if iteration % 10 == 0:
            print("iteration=%d" % iteration)
            sys.stdout.flush()
    return run_time_list


def sweep_n_for_dicts(n: int, m:int, skip:int) -> list:
    iteration = 0

    run_time_list = []
    keys_not_yet_in_dict = list(range(0, n))  # keys to insert.
    shuffle(keys_not_yet_in_dict)
    keys = []
    dicts = [dict() for _ in range(m)]

    for j in range(1, n, skip):
        iteration += 1
        while len(dicts[0]) < j:
            k = keys_not_yet_in_dict.pop()
            v = randint(0, 100000)
            for d in dicts:
                d[k] = v
            keys.append(k)   # keys known to be in the dicts.
            assert len(keys) == len(dicts[0])

        # pick a random key and swap it to the end and remove it by popping.
        i = randint(0, len(keys)-1)
        keys[i], keys[-1] = keys[-1], keys[i]
        removekey = keys.pop()

        start_time_secs = time.time()
        for d in dicts:   # there are m dicts.
            del d[removekey]
        end_time_secs = time.time()

        elapsed_secs = end_time_secs - start_time_secs
        run_time_list.append(elapsed_secs / m)

        if iteration % 10 == 0:
            print("iteration=%d" % iteration)
            sys.stdout.flush()
    return run_time_list


def main():

    list_run_time_list = sweep_n_for_lists(N, M, SKIP)
    dict_run_time_list = sweep_n_for_dicts(N, M, SKIP)
    plt.scatter(range(1, N+1, SKIP), list_run_time_list, color="blue")
    plt.scatter(range(1, N+1, SKIP), dict_run_time_list, color="red")

    plt.title('Execution time of del vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

main()