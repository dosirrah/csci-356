# import sys
import matplotlib.pyplot as plt
import time

def f(i):
    if i == 0:
        # print("reached terminating condition")
        return
    # print(f"f({i})")
    # sys.stdout.flush()
    f(i-1)



f(4)

N=30
M=10000


def main():
    run_times = []
    for i in range(N):
        start_time = time.time()
        for _ in range(M):
            f(i)
        end_time = time.time()
        elapsed_time = end_time - start_time
        avg_elapsed_time = elapsed_time / M
        run_times.append(avg_elapsed_time)

    plt.scatter(range(1, N+1), run_times, color="blue")

    plt.title('Run time vs. N')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')
    plt.ylim(bottom=0)

    plt.show()

main()