from binary_search_tree import BinarySearchTree
import matplotlib.pyplot as plt
from random import randint
from time import time
import gc
import sys


# def populate_tree(n: int) -> BinarySearchTree:
#     t = BinarySearchTree()
#     for _ in range(n):
#         k, v = randint(0, 10000), randint(0, 10000)
#         t.put(k, v)


def perf_test_search(n: int, m: int) -> list:
    gc.disable()
    trees = []
    res = []
    for _ in range(m):
        trees.append(BinarySearchTree())

    for i in range(1, n):
        for t in trees:
            k, v = randint(0, n*10), randint(0, 10000)
            t.put(k, v)

        start_time = time()
        for t in trees:
            try:
                t.find(randint(0, n*10))
            except KeyError:
                pass
        end_time = time()
        elapsed_time = end_time - start_time
        res.append(elapsed_time / m)

        if i % 1000 == 0:
            sys.stdout.write(f"{i}")
            sys.stdout.flush()
        elif i % 100 == 0:
            sys.stdout.write(".")
            sys.stdout.flush()

    gc.enable()
    return res


def worst_case_perf_search(n, m):
    gc.disable()
    trees = []
    res = []
    t = BinarySearchTree()

    for i in range(1, n):
        k, v = i, randint(0, 10000)
        t.put(k, v)

        start_time = time()
        for _ in range(m):
            try:
                # t.find(randint(1, n))
                t.find(n+1)  # guarantee a miss.
            except KeyError:
                pass
        end_time = time()
        elapsed_time = end_time - start_time
        res.append(elapsed_time / m)

        if i % 1000 == 0:
            sys.stdout.write(f"{i}")
            sys.stdout.flush()
        elif i % 100 == 0:
            sys.stdout.write(".")
            sys.stdout.flush()


    gc.enable()
    return res



if __name__ == "__main__":

    def main():
        # n = 100000
        # m = 10
        # run_times = perf_test_search(n, 10)
        # plt.scatter(range(1, n), run_times, color="red")
        #
        # plt.title('Average search time vs. N')
        # plt.xlabel('N')
        # plt.ylabel('t (seconds)')
        # plt.ylim(bottom=0)
        #
        # plt.show()

        n = 100
        m = 100
        run_times = worst_case_perf_search(n, m)
        plt.scatter(range(1, n), run_times, color="red")

        plt.title('Average search time vs. N')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(bottom=0)

        plt.show()

    main()