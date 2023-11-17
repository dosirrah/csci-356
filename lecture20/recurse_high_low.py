from __future__ import annotations


def recurse(sorted_list, target, low, high) -> int | None:
    """
    find whether the target value is in the sorted list using binary search.
    """

    if low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            return recurse(sorted_list, target, mid + 1, high)
        return recurse(sorted_list, target, low, mid -1)
    return None   # not found.

def recurse_high_low(sorted_list, target):
    return recurse(sorted_list, target,0, len(sorted_list)-1)


if __name__ == "__main__":
    from bisect import bisect_left
    import matplotlib.pyplot as plt
    from lecture08.high_low import high_low
    import random
    import sys
    import time

    M = 100    # number of times to repeat a call to get a good measurement.
    BIGINT = 100000000
    N = range(1, 1000000, 10000)  # vary N from 1 to a 1000 with a step of 10.


    def perf_test(f:callable)-> list:
        run_time_list = []
        for n in N:
            print("n=%d" % n)
            sys.stdout.flush()  # make sure it outputs the above line right away.
            lst = []
            for i in range(n):
                lst.append(random.randint(1, BIGINT))
            lst = sorted(lst)  # sort into increasing order

            start_time = time.time()  # seconds since 00:00:00 UTC on January 1, 1970.
            for _ in range(M):
                target = random.randint(1, BIGINT)
                f(lst, target)
            end_time = time.time()
            elapsed_secs = end_time - start_time
            run_time_list.append(elapsed_secs/M)
        return run_time_list

    def main():
        recurse_run_time_list = perf_test(recurse_high_low)
        plt.scatter(N, recurse_run_time_list, color="red")

        run_time_list = perf_test(high_low)
        plt.scatter(N, run_time_list, color="blue")

        bisect_run_time_list = perf_test(bisect_left)
        plt.scatter(N, bisect_run_time_list, color="green")

        plt.title('Average execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')

        plt.show()

        # recurse_run_time_list = perf_test(recurse_high_low)
        # plt.scatter(N, recurse_run_time_list, color="red")
        #
        # plt.title('Average execution times for recurse_high_low')
        # plt.xlabel('N')
        # plt.ylabel('t (seconds)')
        #
        # plt.show()



    main()