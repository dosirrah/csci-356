class HashTable:
    def __init__(self, capacity: int = 11, max_load: float = 0.5):
        """

        :param capacity: starting size of the hash table.
        :param max_load:
        """
        self._capacity = capacity
        self._slots = [None] * self._capacity
        self._data = [None] * self._capacity
        self._max_load = max_load
        self._len = 0

    def _grow(self):
        self._capacity *= 2
        slots = self._slots
        self._slots = [None] * self._capacity
        data = self._data
        self._data = [None] * self._capacity

        for i in range(len(slots)):
            if slots[i] is not None:
                self.put(slots[i], data[i])

    def put(self, key, data):
        self._len += 1
        load = float(self._len) / self._capacity
        if load > self._max_load:
            self._grow()

        hashvalue = HashTable._hashfunction(key, len(self._slots))
        if self._slots[hashvalue] is None:
            self._slots[hashvalue] = key
            self._data[hashvalue] = data
        else:
            if self._slots[hashvalue] == key:
                self._data[hashvalue] = data  # replace
            else:
                nextslot = HashTable._rehash(hashvalue, len(self._slots))
                while self._slots[nextslot] is not None and \
                        self._slots[nextslot] != key:
                    nextslot = HashTable._rehash(nextslot, len(self._slots))

                if self._slots[nextslot] is None:
                    self._slots[nextslot] = key
                    self._data[nextslot] = data
                else:
                    self._data[nextslot] = data  # replace

    def get(self, key):
        startslot = self._hashfunction(key, len(self._slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self._slots[position] is not None and \
                not found and not stop:
            if self._slots[position] == key:
                found = True
                data = self._data[position]
            else:
                position = self._rehash(position, len(self._slots))
                if position == startslot:
                    stop = True
            return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        return self._len

    @staticmethod
    def _hashfunction(key, size):
        return key % size

    @staticmethod
    def _rehash(oldhash, size):
        return (oldhash + 1) % size


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
    M = 1000

    def perf_test_hash_table(capacity, max_load_factor):
        put_run_time_list = []
        get_run_time_list = []

        keys = [random.randint(1, BIGINT) for _ in range(N)]
        values = [random.randint(1, BIGINT) for _ in range(N)]

        htables = [HashTable(capacity, max_load_factor) for _ in range(M)]

        for n in range(1, N):
            start_time = time.time()  # seconds since 00:00:00 UTC on January 1, 1970.
            for h in htables:
                h.put(keys[n], values[n])
            end_time = time.time()

            elapsed_secs = end_time - start_time
            put_run_time_list.append(elapsed_secs / M)

            start_time = time.time()  # seconds since 00:00:00 UTC on January 1, 1970.
            for h in htables:
                # k = keys[random.randint(0, n-1)]
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

        return put_run_time_list, get_run_time_list

    def main():

        # capacity is made large enough to never require resizing.
        # The max_load_factord is also set high enough so that the table becomes
        # almost entirely full.
        capacity = N + 1

        put_run_time_list, get_run_time_list = perf_test_hash_table(capacity, 1.0)
        plt.scatter(range(1, N), put_run_time_list, color="green")
        plt.title(f'Average put execution times (max load 1.0)')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.show()

        plt.scatter(range(1, N), get_run_time_list, color="green")
        plt.title('Average get execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.show()

        put_run_time_95_list, get_run_time_95_list = \
            perf_test_hash_table(3, 0.95)
        plt.scatter(range(1, N), put_run_time_95_list, color="green", label="max_load=0.95")
        put_run_time_50_list, get_run_time_50_list = \
            perf_test_hash_table(3, 0.5)
        plt.scatter(range(1, N), put_run_time_50_list, color="red", label="max_load=0.5")
        plt.title('Average put execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.legend()
        plt.show()

        plt.scatter(range(1, N), put_run_time_95_list, color="green", label="max_load=0.95")
        plt.scatter(range(1, N), put_run_time_50_list, color="red", label="max_load=0.5")
        plt.title('Average put execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.ylim(0, 0.000004)
        plt.legend()
        plt.show()

        plt.scatter(range(1, N), put_run_time_95_list, color="green",
                    label="max_load=0.95")
        plt.scatter(range(1, N), put_run_time_50_list, color="red",
                    label="max_load=0.5")
        plt.yscale('log')
        plt.title('Average put execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.legend()
        plt.show()

        # plt.scatter(range(1, N), get_run_time_list, color="red")
        # plt.title('Average get execution times')
        # plt.xlabel('N')
        # plt.ylabel('t (seconds)')
        # plt.legend()
        # plt.show()

    main()
