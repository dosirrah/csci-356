import random
from time import time
from matplotlib import pyplot as plt
from queue import Queue


def main(n: int, m: int) -> None:
    queues = [Queue() for _ in range(m)]
    average_time = []
    for _ in range(n):
        start = time()
        for x in queues:
            x.enqueue(random.randint(0, n))
        end = time()
        milliseconds = (end-start)/m * 1000
        average_time.append(milliseconds)

    plt.scatter(range(1, n+1), average_time)
    plt.xlabel("Number of Execution")
    plt.ylabel("Average Enqueue Time (ms)")
    plt.show()
    print(average_time)


main(10000, 50)





