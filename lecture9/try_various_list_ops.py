"""Big-O denotes an upper bound.  It can be a loose upper bound meaning the
algorithm always performs better for large n than indiciated by the big-O
notation used to describe an algorithm.   Even when the upper bound is
a tight upper bound, big-oh is considered to be the "worst case." """

from random import randint
import sys
import time


def f(x: list):
    # perform some operation on f.

    # test [] operator.
    i = randint(0, len(x)-1)    # O(1)
    y = x[i]          # give me the ith item.  O(1)
    # z = x.index(y)   # finds y.  What time complexity O(?)
    return y

    # try other ops HERE ...

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    M = 100  # number of times to execute an operation to get a reasonable average.

    def sweep_n(n_range) -> list:
        run_time_list = []
        for n in N:
            print("entire n=%d" % n)
            sys.stdout.flush()
            x = [randint(0, 1000000) for _ in range(n)]

            start_time = time.time()
            for _ in range(M):

                # should take O(n) except we limited the search to an element near the front.
                f(x)

            end_time = time.time()
            elapsed_secs = end_time - start_time
            run_time_list.append(elapsed_secs/M)

        return run_time_list


    def main():
        global N
        run_time_list = []
        N = range(10, 10000000, 100000)  # vary N from 1 to a 10000 with a step of 50.

        run_time_list2 = sweep_n(N)
        plt.scatter(N, run_time_list2, color="blue")

        plt.title('Execution time')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')

        plt.show()


    main()
