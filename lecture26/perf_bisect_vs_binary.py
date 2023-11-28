"""In this file I perform a performance comparison of searching a
sorted array vs. a randomized binary tree."""
import matplotlib.pyplot as plt

from lecture26.binary_search_tree_set import BinarySearchTreeSet
from random import shuffle, randint
from bisect import bisect_left
from time import time
import sys


def randomized_binary_search_tree(arr):
    shuffle(arr)
    set = BinarySearchTreeSet()
    for k in arr:
        set.add(k)


def perf_bisect(n, m):
    keys = [randint(1, 100)]
    results = []
    for i in range(0, n):

        # perform m random searches
        start_secs = time()
        for _ in range(m):
            k = keys[randint(0, len(keys)-1)]
            bisect_left(keys, k)
        end_secs = time()
        elapsed_secs = end_secs - start_secs
        results.append(elapsed_secs / m)
        keys.append(keys[-1] + randint(1, 100))

    return results


def perf_bst(n, m):
    keys = []
    results = []

    tree = BinarySearchTreeSet()
    for i in range(n):
        keys.append(randint(0, 10000))
        tree.add(keys[-1])

        start_secs = time()
        for _ in range(m):
            k = keys[randint(0, len(keys)-1)]
            assert k in tree
        end_secs = time()
        elapsed_secs = end_secs - start_secs
        results.append(elapsed_secs / m)

        if i % 100 == 0:
            sys.stdout.write(f"{i}")
        elif i % 20 == 0:
            sys.stdout.write(".")

    return results

if __name__ == "__main__":

    def main():
        n = 1000
        m = 5000
        run_times = perf_bst(n, m)
        plt.scatter(range(1, n + 1), run_times, color="red", label="bst")

        run_times = perf_bisect(n, m)
        plt.scatter(range(1, n + 1), run_times, color="green", label="bisect")

        plt.title('Run time vs. N')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(bottom=0)

        plt.legend()
        plt.show()


    main()