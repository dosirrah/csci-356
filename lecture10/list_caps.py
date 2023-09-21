
from random import randint
import sys
import time


def sweep_cap(n:int) -> list:
    my_list = []
    caps = []
    caps.append(sys.getsizeof(my_list))
    for i in range(n):
        my_list.append(i)
        caps.append(sys.getsizeof(my_list))
    return caps

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    N=1000000
    def main():
        global N

        caps = sweep_cap(N)
        plt.scatter(range(0, N+1), caps, color="blue")

        plt.title('List capacity')
        plt.xlabel('N')
        plt.ylabel('capacity')

        plt.show()

    main()