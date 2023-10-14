
import gc
import matplotlib.pyplot as plt
from random import randint
from list_queue import ListQueue
from sll_queue import SLLQueue
from cb_queue import CBQueue
import sys
import time

# how many queues we have of a given length N.
M = 100
N = 10000


def perf_test_queue(class_object) -> (list, list):
    global N, M

    queues = []
    for i in range(M):
        queues.append(class_object())

    enqueue_run_times = []

    # performance test enqueues.
    for n in range(1, N+1):
        start_time_secs = time.time()
        for i in range(M):
            x = randint(0, 100000)
            queues[i].enqueue(x)
        end_time_secs = time.time()

        avg_elapsed_secs = (end_time_secs - start_time_secs) / M
        enqueue_run_times.append(avg_elapsed_secs)

        if n % 10 == 0:
            print(".")
            sys.stdout.flush()
        if n % 100 == 0:
            print(n)
            sys.stdout.flush()

    dequeue_run_times = [0.] * N
    while len(queues[0]) > 0:
        n = len(queues[0])
        start_time_secs = time.time()
        for q in queues:
            _ = q.dequeue()
        end_time_secs = time.time()

        avg_elapsed_secs = (end_time_secs - start_time_secs) / M
        dequeue_run_times[n-1] = avg_elapsed_secs

    return enqueue_run_times, dequeue_run_times


def main():
    lq_enqueue_secs, lq_dequeue_secs = perf_test_queue(ListQueue)

    plt.scatter(range(1, N+1), lq_enqueue_secs, color="blue")

    plt.title('Python list run time of enqueue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    plt.scatter(range(1, N+1), lq_dequeue_secs, color="blue")

    plt.title('Python list run time of dequeue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    sll_enqueue_secs, sll_dequeue_secs = perf_test_queue(SLLQueue)
    plt.scatter(range(1, N+1), sll_enqueue_secs, color="red")

    plt.title('linked list run time of enqueue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    plt.scatter(range(1, N+1), sll_dequeue_secs, color="red")

    plt.title('linked list run time of dequeue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    gc.disable()
    sll_enqueue_secs, sll_dequeue_secs = perf_test_queue(SLLQueue)
    gc.enable()
    plt.scatter(range(1, N+1), sll_enqueue_secs, color="purple")

    plt.title('No-GC linked list run time of enqueue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    plt.scatter(range(1, N+1), sll_dequeue_secs, color="purple")

    plt.title('No-GC linked list run time of dequeue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()
    #
    # cb_enqueue_secs, cb_dequeue_secs = perf_test_queue(CBQueue)
    # plt.scatter(range(1, N+1), cb_enqueue_secs, color="green")
    #
    # plt.title('Execution time of enqueue vs. N')
    # plt.xlabel('N')
    # plt.ylabel('t (seconds)')
    # plt.ylim(bottom=0)
    #
    # plt.show()
    #
    # plt.scatter(range(1, N+1), cb_dequeue_secs, color="green")
    #
    # plt.title('Execution time of dequeue vs. N')
    # plt.xlabel('N')
    # plt.ylabel('t (seconds)')
    # plt.ylim(bottom=0)
    #
    # plt.show()


main()


