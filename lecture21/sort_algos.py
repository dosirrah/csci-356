
import matplotlib.pyplot as plt
import random
import sys
import time

def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def selection_sort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertion_sort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue



# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# selectionSort(alist)
# insertionSort(alist)
# mergeSort(alist)
# print(alist)

# N=400
N = 26
M = 100
BIGINT = 100


def perf_test(sort):

    # M=fx
    run_times = []
    alists = [list() for _ in range(M)]

    for i in range(N):
        for a in alists:
            a.append(random.randint(0, BIGINT))
            random.shuffle(a)

        start_time = time.time()
        for a in alists:
            sort(a)
        end_time = time.time()
        elapsed_time = (end_time - start_time) / M
        run_times.append(elapsed_time)

        if i % 100 == 0:
           sys.stdout.write(f"{i}")
           sys.stdout.flush()
        elif i % 5 == 0:
           sys.stdout.write(".")
           sys.stdout.flush()

    return run_times

if __name__ == "__main__":

    def main():

        # run_times = perf_test(bubble_sort)
        # plt.scatter(range(1, N + 1), run_times, color="blue")

        run_times = perf_test(selection_sort)
        plt.scatter(range(1, N + 1), run_times, color="red")

        run_times = perf_test(insertion_sort)
        plt.scatter(range(1, N + 1), run_times, color="green")

        plt.title('Run time vs. N')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(bottom=0)

        plt.show()


    main()