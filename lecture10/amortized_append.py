"""I used this code to poke around trying to figure out the time complexity
of Python's built-in list."""

from random import randint
import sys
import time


def sweep_n(n: int, m: int) -> list:
    """
    Measure the execution time of adding the
    nth item to a list.  We create m separate lists,
    perform the nth item insertion in all of the
    m lists and measure the time elapsed across all
    m lists.  This allows us average the run time
    across m insertions but all to lists of the
    same size so that each time we are measuring the
    time for adding the nth item.

    I was expecting to see a jump in execution time for
    certain values of n, which I would expect to occur
    when the underlying array is reallocated and the
    items are copied from the old array into the new one.

    :param n: sweep appending an item to all sizes of lists from 0 to n.
    :param m: number of times to measure a single append in order
          to get a reasonable average.
    :return: a list of average append times where the ith floating
          point in the list corresponds to
    """
    run_time_list = [0.] * n

    x = [randint(0, 1000000) for _ in range(n)]
    y = []

    # create m lists.  We will grow all lists one at a time and measure
    # the time of adding an nth element ot a list by averaging the
    # append time across all of the lists.
    for _ in range(m):
        y.append(list())

    for n in range(1, n):
        if n % 10 == 0:
            print("sweep n: %d" % n)
            sys.stdout.flush()
        v = x[n-1]
        start_time = time.time()
        for i in range(m):
            y[i].append(v)   # measuring performance of append.
        end_time = time.time()
        elapsed_secs = end_time - start_time
        run_time_list[n] = elapsed_secs

    # because we performed each append M times, we divide the elapsed
    # time by M in order to get an average.
    run_time_list = [x / M for x in run_time_list]
    return run_time_list


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    M = 1000000  # number of times to execute an operation to get a reasonable average.
    N = 200

    def main():
        global N, M

        run_time_list = sweep_n(N, M)
        plt.scatter(range(1, N), run_time_list[1:], color="blue")

        plt.title('Execution time of an append operation vs. N')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(bottom=0)

        plt.show()


    main()
