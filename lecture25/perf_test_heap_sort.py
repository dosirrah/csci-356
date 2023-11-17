from lecture22to23.fast_sort_algos import quick_sort
from heap_sort import heap_sort, heap_sort_pushes
from lecture21.sort_algos import perf_test
import matplotlib.pyplot as plt


if __name__ == "__main__":

    def main():
        n = 200
        hs_run_times = perf_test(heap_sort, n)
        plt.scatter(range(1, n + 1), hs_run_times, color="red")

        hsp_run_times = perf_test(heap_sort_pushes, n)
        plt.scatter(range(1, n + 1), hsp_run_times, color="green")

        plt.title('Run time vs. N')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(bottom=0)

        plt.show()

        run_times = perf_test(quick_sort, n)
        plt.scatter(range(1, n + 1), run_times, color="blue")
        plt.scatter(range(1, n + 1), hs_run_times, color="red")
        plt.scatter(range(1, n + 1), hsp_run_times, color="green")

        plt.title('Run time vs. N')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(bottom=0)

        plt.show()


    main()