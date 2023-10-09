"""Implementation of a bag using a list.

This is an example of how someone would NOT implement a Bag.
It is useful to illustrate the growth in execution times as a fucnction
of the number of items in a bag with a slow (poor) implementation compared to
a fast implementation.

"""
from __future__ import annotations   # allows me specify list|None as type hint for items.

class BagList:

    def __init__(self, items: list|None = None):
        """
        :param items: The initial items placed in the bag.  This defaults to None.
            The items argument must be iterable.
        """
        # The internal representation of the bag is a defaultdict.  A defaultdict(int)
        # creates a default initialized in integer whenever a key is looked up if the
        # key does not already exist.  A default initialized integer has a value of zero.
        self._contents = []

        if items is not None and len(items) > 0:
            self._contents.extend(items)

    def __len__(self):   # if x is a Bag __len__ called when len(x)
        return len(self._contents)

    def __contains__(self, item) -> bool: # if x is a Bag __contains__ called with "in"
        return item in self._contents

    def add(self, item):
        """
        Add the passed item to the bag.

        The item must be comparable meaning it has an __eq__ method.

        Equivalence is determined by the __eq__ methods (i.e., == operator).

        :param item: item that will be inserted.
        :return: None
        """
        # seems a bit redundant, but this class only exists for comparison to bag.
        self._contents.append(item)

    def remove(self, item) -> None:
        """
        remove one instance of the passed item.

        :param item: item to be removed.
        :raises KeyError: if the item about to be removed is not in the Bag.
        """
        if item not in self._contents:
            raise KeyError

        self._contents.remove(item)

    def discard(self, item) -> None:
        """
        if item is present then remove one instance of the passed item.  If the key is not present
        then do nothing and do not raise an exception.
        :param item: item to be removed.
        :return: None
        """
        if item not in self._contents:
            return

        self._contents.remove(item)


    def removeall(self, item) -> None:
        """
        Remove all instances of item from the list.  Raises KeyError if not found.
        :param item: item to be removed.
        :return: None
        :raises KeyError: if item is not in the list.
        """
        # removes all that match.
        if item not in self._contents:
            raise KeyError

        self._contents = [x for x in self._contents if not (x == item)]

    def discardall(self, item) -> None:
        """
        Discard all instances of item from the bag.

        An item is discarded if it equal according to the item's
        __eq__ method (i.e., the == operator).

        :param item: item to be removed
        :return: None
        """
        # discards all that match based on the == operator.
        self._contents = [x for x in self._contents if not (x == item)]

    def count(self, item) -> int:
        """
        Return number of instances of item
        :param item: item to count
        :return: the number of instances of item in the bag.
        """
        return self._contents.count(item)

    def __iter__(self):
        return iter(self._contents)

    def __repr__(self) -> str:
        return "BagList({" + ", ".join([repr(i) for i in self]) + "})"




if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import time
    import random
    import sys
    from bag import Bag

    M = 10   # number of times to run an experiment.
    N = 10000  # max size of bag within experiment
    def main():
        # add some examples here.
        # b = BagList([5,6,6])
        # print(b)

        print("measuring count() on BagList")
        bl_times = []
        for n in range(1, N, 100):
            bl = BagList()
            for _ in range(n):
                bl.add(random.randint(1,10))
            assert len(bl) == n
            start_time = time.time()
            for repeats in range(M):
                # test the count operation.
                bl.count(random.randint(1,10))
            end_time = time.time()
            if (n-1) % 500 == 0:
                print("n:", n)
                sys.stdout.flush()
            bl_times.append((end_time - start_time)/M)

        # now measure the same operation for Bag.
        print("measuring count() on Bag")
        b_times = []
        for n in range(1, N, 100):
            b = Bag()
            for _ in range(n):
                b.add(random.randint(1, 10))
            start_time = time.time()  # time in seconds
            for repeats in range(M):
                # test the count operation.
                b.count(random.randint(1, 10))
            end_time = time.time()
            if (n-1) % 500 == 0:
                print("n:", n)
                sys.stdout.flush()

            b_times.append((end_time - start_time)/M)

        x = range(1,N, 100)
        plt.scatter(x, bl_times, color="blue")
        plt.scatter(x, b_times, color="red")

        plt.title('Execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')

        plt.show()


        # N = 1000
        # M = 10
        # b_times = []
        # for n in range(1, N, 10):
        #     start_time = time.time()  # time in seconds
        #     for repeats in range(M):
        #        b = Bag()
        #        for _ in range(n):
        #            b.add(random.randint(1, 10))
        #     end_time = time.time()
        #     b_times.append((end_time - start_time)/(M*n))
        #
        # x = range(1, N, 10)
        # plt.scatter(x, b_times, color="red")
        # plt.title('Execution times')
        # plt.xlabel('N')
        # plt.ylabel('t (seconds)')
        # plt.show()

    main()