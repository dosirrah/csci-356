"""In this example, we measure the average execution time of a key-lookup
into a dict.  By dict I am referrring to Python's built-in dict data structure."""

from random import randint
import sys
import time

def lookup(keys, d):
    """
    Perform a single lookup on the dict for a random key.

    I store the keys I want to lookup in a list
    because we have already studied the performance of Python's
    built-in list.  We know that retrieving the ith key in a item
    in a list takes O(1) time.

    What I want to confirm is that a dict lookup is also O(1).
    """
    k = keys[randint(0, len(keys)-1)]   # O(1) lookup into a list.
    _ = d[k]                            # O(?)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    M = 1000  # number of times to execute an operation to get a reasonable average.

    def sweep_n(n_range) -> list:
        run_time_list = []
        for n in N:
            print("entire n=%d" % n)
            sys.stdout.flush()
            keys = [randint(0, 1000000) for _ in range(n)]
            d = {}
            for k in keys:
                d[k] = randint(0, 100000)

            start_time = time.time()

            # we perform M lookups and then compute the average
            # over those M loookups.
            for _ in range(M):
                lookup(keys, d)

            end_time = time.time()
            elapsed_secs = end_time - start_time
            run_time_list.append(elapsed_secs/M)

        return run_time_list


    def main():
        global N
        run_time_list = []
        N = range(1, 100000, 1000)  # vary N from 1 to a 10000 with a step of 50.

        run_time_list2 = sweep_n(N)
        plt.scatter(N, run_time_list2, color="blue")

        plt.title('Execution time doing random key lookups')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(bottom=0)

        plt.show()


    main()
