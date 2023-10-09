"""EXample of functions that take differing amount of times.
"""

import sys


def f(n:int)-> None:
    x = 0                   # 1 step

    for i in range(n):      # loop runs next step n times.
        print("n=%d" % n)
        sys.stdout.flush()
        for j in range(n):
            for k in range(n):
                x += 5              # 1 step


# Remember: I only execute the "main" part of my script if I run various_run_times.py
# directly, e.g.,
#   $ python3 various_run_times.py
#
# I could still import various_run_times.py into another module, such as
# module containing unit tests.  When I run the test module, main() from
# this file would not get executed.
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import time

    M = 100    # number of times to repeat a call to get a good measurement.

    def main():
        run_time_list = []
        N = range(1, 1000, 50)  # vary N from 1 to a 1000 with a step of 10.
        for n in N:
            start_time = time.time()  # seconds since 00:00:00 UTC on January 1, 1970.
            f(n)
            end_time = time.time()
            elapsed_secs = end_time - start_time
            run_time_list.append(elapsed_secs)

        plt.scatter(N, run_time_list, color="blue")

        plt.title('Execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')

        plt.show()


    # I don't want to pollute the global namespace with many different
    # variable names, so I call a function main() in which all of my variables
    # are locals.
    main()
