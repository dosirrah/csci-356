import matplotlib.pyplot as plt


def merge_sort(alist):
    # print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    # print("Merging ",alist)


def quick_sort(arr):
    def _sort(first, last):
        if first < last:
            splitpoint = partition(arr, first, last)
            _sort(first, splitpoint - 1)  # left "half"
            _sort(splitpoint + 1, last)   # right "half"

    _sort(0, len(arr) - 1)


def partition(arr, first, last):
    pivotvalue = arr[first]
    i = first + 1
    j = last
    while True:
        while i <= j and arr[i] <= pivotvalue:
            i += 1
        while arr[j] >= pivotvalue and j >= i:
            j -= 1
        if j < i:
            break
        else:  # swap
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[first] = arr[first], arr[j]
    return j

# alist = [54,26,93,17,77,31,44,55,20]
# quickSort(alist)
# print(alist)
#
# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)


if __name__ == "__main__":
    # from lecture21.sort_algos import selection_sort
    from lecture21.sort_algos import insertion_sort
    from lecture21.sort_algos import perf_test, N

    def main():

        run_times = perf_test(quick_sort)
        plt.scatter(range(1, N + 1), run_times, color="blue")

        # run_times = perf_test(merge_sort)
        # plt.scatter(range(1, N + 1), run_times, color="purple")

        # run_times = perf_test(selection_sort)
        # plt.scatter(range(1, N + 1), run_times, color="red")
        #
        run_times = perf_test(insertion_sort)
        plt.scatter(range(1, N + 1), run_times, color="green")

        plt.title('Run time vs. N')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(bottom=0)

        plt.show()

    main()
