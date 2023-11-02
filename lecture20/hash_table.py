class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity
        self._slots = [None] * self._capacity
        self._data = [None] * self._capacity

    def put(self,key,data):
        hashvalue = self.hashfunction(key, len(self._slots))

        if self._slots[hashvalue] is None:
            self._slots[hashvalue] = key
            self._data[hashvalue] = data
        else:
            if self._slots[hashvalue] == key:
                self._data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue, len(self._slots))
                while self._slots[nextslot] != None and \
                              self._slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self._slots))

                if self._slots[nextslot] == None:
                    self._slots[nextslot]=key
                    self._data[nextslot]=data
                else:
                    self._data[nextslot] = data #replace

    def get(self, key):
        startslot = self.hashfunction(key, len(self._slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self._slots[position] != None and \
                               not found and not stop:
            if self._slots[position] == key:
                found = True
                data = self._data[position]
            else:
                position = self.rehash(position, len(self._slots))
                if position == startslot:
                    stop = True
            return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import random
    import sys
    import time


    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


    def next_prime(n):
        """Return the next prime greater than n."""
        prime = n
        found = False
        while not found:
            prime += 1
            if is_prime(prime):
                found = True
        return prime

    BIGINT = 100000000
    N = next_prime(1000)-1
    M = 100
    put_run_time_list = []
    get_run_time_list = []
    keys = [random.randint(1, BIGINT) for _ in range(N)]
    values = [random.randint(1, BIGINT) for _ in range(N)]

    capacity = N+1
    htables = [HashTable(capacity) for _ in range(M)]

    for n in range(1, N):
        start_time = time.time()  # seconds since 00:00:00 UTC on January 1, 1970.
        for h in htables:
            h.put(keys[n], values[n])
        end_time = time.time()

        elapsed_secs = end_time - start_time
        put_run_time_list.append(elapsed_secs / M)

        start_time = time.time()  # seconds since 00:00:00 UTC on January 1, 1970.
        for h in htables:
            #k = keys[random.randint(0, n-1)]
            k = keys[n]
            h.get(k)
        end_time = time.time()
        elapsed_secs = end_time - start_time
        get_run_time_list.append(elapsed_secs / M)

        if n % 100 == 0:
            sys.stdout.write(f"{n}")
        elif n % 10 == 0:
            sys.stdout.write(".")
            sys.stdout.flush()

    plt.scatter(range(1, N), put_run_time_list, color="green")

    plt.title('Average put execution times')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')

    plt.show()

    plt.scatter(range(1, N), get_run_time_list, color="green")

    plt.title('Average get execution times')
    plt.xlabel('N')
    plt.ylabel('t (seconds)')

    plt.show()


    # put_run_time_list = []
    # get_run_time_list = []
    # for n in N:
    #     h = HashTable(next_prime(n*2))
    #     print("n=%d" % n)
    #     sys.stdout.flush()  # make sure it outputs the above line right away.
    #
    #     keys = [random.randint(1, BIGINT) for _ in range(n)]
    #     values = [random.randint(1, BIGINT) for _ in range(n)]
    #     start_time = time.time()  # seconds since 00:00:00 UTC on January 1, 1970.
    #     for i in range(n):
    #         h.put(keys[i], values[i])
    #     end_time = time.time()
    #
    #     elapsed_secs = end_time - start_time
    #     put_run_time_list.append(elapsed_secs / n)
    #
    #     start_time = time.time()  # seconds since 00:00:00 UTC on January 1, 1970.
    #     for k in keys:
    #         h.get(k)
    #     end_time = time.time()
    #     elapsed_secs = end_time - start_time
    #     get_run_time_list.append(elapsed_secs / len(keys))
    #
    # plt.scatter(N, put_run_time_list, color="red")
    #
    # plt.title('Average put execution times')
    # plt.xlabel('N')
    # plt.ylabel('t (seconds)')
    #
    # plt.show()
    #
    # plt.scatter(N, get_run_time_list, color="red")
    #
    # plt.title('Average get execution times')
    # plt.xlabel('N')
    # plt.ylabel('t (seconds)')
    #
    # plt.show()

