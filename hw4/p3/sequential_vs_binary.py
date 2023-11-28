from time import time
from matplotlib import pyplot as plt
from random import randint
from bisect import bisect_left
import sys


def perf_sequential_search(n: int, m: int) -> list:
    """

    :param n: maximum n to test.
    :param m: number of times to run each test in order to generate an average
    :return:  list where the ith element corresponds to the averate time to
      search for n-1, i.e., i=0=n-1 means n=1.
    """

    run_times_secs = []
    lists = [list() for _ in range(m)]
    for i in range(1, n+1):
        for x in lists:
            x.append(randint(0, 1000))

        start_secs = time()
        for x in lists:
            k = x[randint(0, len(x)-1)]
            x.index(k)  # linear search.
        end_secs = time()
        elapsed_secs = end_secs - start_secs
        run_times_secs.append(elapsed_secs / m)

        if i % 100 == 0:
            sys.stdout.write(f"{i}")
        elif i % 20 == 0:
            sys.stdout.write(".")
        sys.stdout.flush()

    sys.stdout.write("\n")
    return run_times_secs


def perf_binary_search(n: int, m: int)-> list:
    # we need to maintain order.  Easy enough.  Always append
    # a larger number than the last in the list.

    run_times_secs = []
    lists = [list() for _ in range(m)]
    for x in lists:
        x.append(randint(0, 100))

    for i in range(1, n+1):

        start_secs = time()
        for x in lists:
            j = randint(0, len(x)-1)   # O(1)
            key = x[j]                    # O(1)
            k = bisect_left(x, key)       # O(log n)
            if j != k:
                assert False
        end_secs = time()
        elapsed_secs = end_secs - start_secs
        run_times_secs.append(elapsed_secs / m)
        for x in lists:
            x.append(x[-1] + randint(1, 100))

        if i % 100 == 0:
            sys.stdout.write(f"{i}")
        elif i % 20 == 0:
            sys.stdout.write(".")
        sys.stdout.flush()
    sys.stdout.write("\n")

    return run_times_secs



def main():
    N = 1000
    M = 100

    seq_run_times = perf_sequential_search(N, M)
    plt.scatter(range(1, N + 1), seq_run_times, color="red", label="sequential search")

    bin_run_times = perf_binary_search(N, M)

    plt.scatter(range(1, N + 1), bin_run_times, color="green", label="binary search")

    # Add note to legend without having a dataset.
    plt.plot([], [], ' ', label=f"avg {M} runs/point")
    plt.title('Run time vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.legend()
    plt.show()

    N = 1000
    M = 10000
    plot_start_secs = time()
    seq_run_times = perf_sequential_search(N, M)
    plt.scatter(range(1, N + 1), seq_run_times, color="red", label="sequential search")
    plt.scatter(range(1, N + 1), bin_run_times, color="green", label="binary search")
    plt.plot([], [], ' ', label=f"avg {M} runs/point")
    plt.title('Run time vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)
    plt.legend()
    plt.show()
    plot_end_secs = time()
    elapsed_secs = plot_end_secs - plot_start_secs
    print(f"Time to plot sequential search for N={N}, M={M} is {elapsed_secs} secs.")

    N = 10000
    M = 1000
    plot_start_secs = time()
    # total cost of generating plots should be O(m log n) assuming rendering
    # the plots take no more than O(n) where n is the number of data points.
    bin_run_times = perf_binary_search(N, M)
    plt.scatter(range(1, N + 1), bin_run_times, color="green", label="binary search")
    plt.plot([], [], ' ', label=f"avg {M} runs/point")
    plt.title('Run time vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.legend()
    plt.show()
    plot_end_secs = time()
    elapsed_secs = plot_end_secs - plot_start_secs
    print(f"Time to plot binary search for N={N}, M={M} is {elapsed_secs} secs.")

main()
