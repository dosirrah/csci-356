import matplotlib.pyplot as plt
import random
import sys
import time


def merge_sort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quick_sort_helper(alist, first, splitpoint - 1)
        quick_sort_helper(alist, splitpoint + 1, last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

# alist = [54,26,93,17,77,31,44,55,20]
# quickSort(alist)
# print(alist)
#
# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)


if __name__ == "__main__":
    from lecture21.sort_algos import selection_sort
    from lecture21.sort_algos import insertion_sort
    from lecture21.sort_algos import perf_test, N, M

    def main():

        run_times = perf_test(quick_sort)
        plt.scatter(range(1, N + 1), run_times, color="blue")

        #run_times = perf_test(merge_sort)
        #plt.scatter(range(1, N + 1), run_times, color="purple")

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
