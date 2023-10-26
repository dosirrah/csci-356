"""Example from 5.5 of *Problem Solving with Data Structures in Python*"""
# from time import sleep

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   # sleep(.001)
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import random
    import time
    import sys

    #print(toStr(1453,16))

    N = 2**64
    M = 5000
    BASE = 2
    SKIP = 10

    run_times = []
    n_values = []
    delta = n = N // 128
    i = 0

    while n < N:
        i += 1
        n += delta
        start_time = time.time()
        for _ in range(M):
            toStr(int(n), BASE)
        end_time = time.time()

        run_times.append((end_time - start_time) * 1000 / M)
        n_values.append(n)

        if i % 10 == 0:
            print("%d toStr: '%s'" % (int(n), toStr(int(n), BASE)))
            sys.stdout.flush()

    plt.scatter(n_values, run_times, color="blue")

    plt.title('Run toStr with base conversion for vs. N digits')
    plt.xlabel('N')
    plt.ylabel('t (ms)')
    plt.ylim(bottom=run_times[0])

    plt.show()




