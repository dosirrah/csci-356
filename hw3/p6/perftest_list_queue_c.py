import gc
import random
from time import time
from matplotlib import pyplot as plt
from queue import Queue

random.seed(123)

def main(n: int, m: int) -> None:
    queues = [Queue() for _ in range(m)]
    average_time = []
    for _ in range(n):
        for x in queues:
            # because pushing to the back is O(1) we don't use
            # enqueue to populate the queues.
            x.items.append(random.randint(0, n))

    gc.disable()
    while len(queues[0]) > 0:
        start_secs = time()
        for x in queues:
            _ = x.dequeue()
        end_secs = time()
        milliseconds = (end_secs-start_secs)/m * 1000
        average_time.append(milliseconds)
    gc.enable()

    average_time.reverse()
    plt.scatter(range(1, n+1), average_time)
    plt.xlabel("Number of Execution")
    plt.ylabel("Average Dequeue Time (ms)")
    plt.show()
    print(average_time)


main(10000, 50)





