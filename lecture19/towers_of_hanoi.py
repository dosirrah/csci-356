def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    # print("moving disk from",fp,"to",tp)
    pass


import matplotlib.pyplot as plt
import time
import math

N=18
M=100
run_times = []
for i in range(N):
    print(f"running {i}")
    start_time = time.time()
    for _ in range(M):
        moveTower(i,"A","B","C")
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_elapsed_time = elapsed_time / M
    run_times.append(avg_elapsed_time)

plt.scatter(range(1, N + 1), run_times, color="blue")

plt.title('Run time vs. N')
plt.xlabel('N')
plt.ylabel('t (seconds)')
plt.ylim(bottom=0)

plt.show()

# try it on a log plot.
log_times = [math.log(t, 10) for t in run_times]
plt.scatter(range(1, N + 1), log_times, color="blue")

plt.title('log run time vs. N')
plt.xlabel('N')
plt.ylabel('log10(t) (seconds)')
#plt.ylim(bottom=0)

plt.show()

#moveTower(3,"A","B","C")