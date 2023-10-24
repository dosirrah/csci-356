from __future__ import annotations

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


def perf_test_queue(class_object, reserve: int | None = None) -> (list, list):
    global N, M

    queues = []
    for i in range(M):
        q = class_object()
        if reserve is not None:
            q.reserve(reserve)
        queues.append(q)

    enqueue_run_times = []
    collections = [[], [], []]        # 3 generations in garbage collector.
    collected = [[], [], []]          # number of objects collected in each generation.
    allocated = [[], [], []]  # 3 generations in garbage collector.
    enq_start_secs = time.time()

    start_gc_stats = gc_stats = gc.get_stats().copy()

    # performance test enqueues.
    for n in range(1, N+1):
        start_time_secs = time.time()
        for i in range(M):
            x = randint(0, 100000)
            queues[i].enqueue(x)
        end_time_secs = time.time()

        avg_elapsed_secs = (end_time_secs - start_time_secs) / M
        enqueue_run_times.append(avg_elapsed_secs)

        if n % 100 == 0:
            sys.stdout.write(".")
            sys.stdout.flush()
        if n % 1000 == 0:
            sys.stdout.write(f"{n}")
            sys.stdout.flush()

        # prev_gc_stats = gc_stats
        gc_stats = gc.get_stats()

        # gc_stats is indexed by generation
        for i, gen in enumerate(gc_stats):
            collections[i].append(gen["collections"] - start_gc_stats[i]["collections"])
            collected[i].append(gen["collected"] - start_gc_stats[i]["collected"])
            allocated[i].append(gc.get_count()[i])

    enq_stop_secs = time.time()
    sys.stdout.write("\n")
    tot_enq_secs = enq_stop_secs - enq_start_secs

    dequeue_run_times = [0.] * N
    deq_start_secs = time.time()

    while len(queues[0]) > 0:
        n = len(queues[0])
        start_time_secs = time.time()
        for q in queues:
            _ = q.dequeue()
        end_time_secs = time.time()

        avg_elapsed_secs = (end_time_secs - start_time_secs) / M
        dequeue_run_times[n-1] = avg_elapsed_secs

    deq_end_secs = time.time()
    tot_deq_secs = deq_end_secs - deq_start_secs

    return enqueue_run_times, dequeue_run_times, tot_enq_secs, tot_deq_secs, \
        collections, collected, allocated


def main():
    lq_enqueue_secs, lq_dequeue_secs, \
        lq_tot_enq_secs, lq_tot_deq_secs, \
        collections, collected, allocated = perf_test_queue(ListQueue)

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

    sll_enqueue_secs, sll_dequeue_secs, \
        sll_tot_enq_secs, sll_tot_deq_secs, \
        collections, collected, allocated = perf_test_queue(SLLQueue)
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

    #plt.scatter(range(1, N+1), collections[0], color="red")
    #plt.scatter(range(1, N+1), collections[1], color="blue")
    plt.scatter(range(1, N+1), collections[2], color="red")
    plt.title("linked list gc collections during enqueue vs. N")
    plt.xlabel('N')
    plt.ylabel('collections')
    plt.ylim(bottom=0)

    plt.show()

    # plt.scatter(range(1, N+1), collected[0], color="red")
    # plt.scatter(range(1, N+1), collected[1], color="blue")
    # plt.scatter(range(1, N+1), collected[2], color="green")
    # plt.title("linked list gc collected during enqueue vs. N")
    # plt.xlabel('N')
    # plt.ylabel('number of garbage collected objects')
    # plt.ylim(bottom=0)
    # plt.show()
    #
    # plt.scatter(range(1, N+1), allocated[0], color="red")
    # plt.scatter(range(1, N+1), allocated[1], color="blue")
    # plt.scatter(range(1, N+1), allocated[2], color="green")
    # plt.title("linked list number of allocated objects during enqueue vs. N")
    # plt.xlabel('N')
    # plt.ylabel('number of allocated objects')
    # plt.ylim(bottom=0)
    # plt.show()

    gc.disable()
    no_gc_sll_enqueue_secs, no_gc_sll_dequeue_secs, \
        no_gc_sll_tot_enq_secs, no_gc_sll_tot_deq_secs, \
        collections, collected, allocated = perf_test_queue(SLLQueue)
    gc.enable()
    plt.scatter(range(1, N+1), no_gc_sll_enqueue_secs, color="purple")

    plt.title('No-GC linked list run time of enqueue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    plt.scatter(range(1, N+1), no_gc_sll_dequeue_secs, color="purple")

    plt.title('No-GC linked list run time of dequeue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    #plt.scatter(range(1, N+1), collections[0], color="red")
    #plt.scatter(range(1, N+1), collections[1], color="blue")
    plt.scatter(range(1, N+1), collections[2], color="purple")
    plt.title("no-gc linked list gc collections during enqueue vs. N")
    plt.xlabel('N')
    plt.ylabel('collections')
    plt.ylim(bottom=0)

    plt.show()

    gc.disable()
    cb_enqueue_secs, cb_dequeue_secs, \
        cb_tot_enq_secs, cb_tot_deq_secs, \
        collections, collected, allocated = perf_test_queue(CBQueue, reserve=N)
    gc.enable()
    plt.scatter(range(1, N+1), cb_enqueue_secs, color="green")

    plt.title('Execution time of enqueue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    plt.scatter(range(1, N+1), cb_dequeue_secs, color="green")

    plt.title('Execution time of dequeue vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

    print(f"total python list enqueue test time elapsed in seconds: {lq_tot_enq_secs}")
    print(f"total python list dequeue test time elapsed in seconds: {lq_tot_deq_secs}")
    print(f"total linked list enqueue test time elapsed in seconds: {sll_tot_enq_secs}")
    print(f"total linked list NO GC enqueue test time elapsed in seconds: {no_gc_sll_tot_enq_secs}")
    print(f"total cbuffer enqueue test time elapsed in seconds: {cb_tot_enq_secs}")
    print(f"total linked list dequeue test time elapsed in seconds: {sll_tot_deq_secs}")
    print(f"total linked list NO GC dequeue test time elapsed in seconds: {no_gc_sll_tot_deq_secs}")
    print(f"total cbuffer dequeue test time elapsed in seconds: {cb_tot_deq_secs}")

main()
