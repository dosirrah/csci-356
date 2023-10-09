def high_low(sorted_list, target):
    """
    find whether the target value is in the sorted list using binary search.
    """

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import random
    import sys
    import time

    M = 100    # number of times to repeat a call to get a good measurement.
    BIGINT = 10000000

    def main():
        run_time_list = []
        N = range(1, 100000, 100)  # vary N from 1 to a 1000 with a step of 10.
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
                high_low(lst, target)
            end_time = time.time()
            elapsed_secs = end_time - start_time
            run_time_list.append(elapsed_secs/M)

        plt.scatter(N, run_time_list, color="blue")

        plt.title('Execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')

        plt.show()

    main()