from collections import defaultdict

class Bag:
    """
    A Bag is similar to a set, but it can contain more than one of the same item.
    For example, a bag can contain

        >>> s = {5,4,9}
        >>> s.add(5)
        >>> s
        {9, 4, 5}

    A Bag is like a mathematical set except that it can hold more than 1 of any given value.

        >>> b = Bag({5,4,9})
        >>> s.add(5)
        >>> s
        Bag({9, 4, 5, 5})

    As with a set, a bag should support fast add, remove and bag membership, i.e.,
    contains.

    """

    def __init__(self, items = None):
        """
        :param items: The initial items placed in the bag.  This defaults to None.
            The items argument must be iterable.
        """
        # The internal representation of the bag is a defaultdict.  A defaultdict(int)
        # creates a default initialized in integer whenever a key is looked up if the
        # key does not already exist.  A default initialized integer has a value of zero.
        self._contents = defaultdict(int)
        self._n = 0

        if items is not None:
            for i in items:
                self._contents[i] += 1
                self._n += 1

    def __len__(self) -> int:   # if x is a Bag __len__ called when len(x)
        """Return the number of items in the bag."""
        return self._n

    def __contains__(self, item) -> bool: # if x is a Bag __contains__ called with "in"
        if item in self._contents:
            return True
        return False

    def add(self, item) -> None:
        """
        Add the passed item to the bag.  If there is an equivalent item already
        in the bag then this merely increases the count of the number of equivalent items.

        The item must be comparable and hashable meaning it must have a __hash__
        method and a __eq__ method.

        Equivalence is determine by the __eq__ methods (i.e., == operator).

        :param item: item that will be inserted.
        :return: None
        """
        self._contents[item] += 1
        self._n += 1

    def remove(self, item) -> None:
        """
        remove one instance of the passed item.

        :raises KeyError: if the item about to be removed is not in the Bag.
        """
        if item not in self._contents:
            raise KeyError

        self._contents[item] -= 1
        self._n -= 1
        if self._contents[item] == 0:
            del self._contents[item]

    def discard(self, item) -> None:
        """
        Same as remove but it doesn't raise a KeyError if item is not
        in the bag. Instead it returns without doing anything.

        :param item:
        :return:
        """
        if item not in self._contents:
                return

        self._n -= 1
        self._contents[item] -= 1

    def removeall(self, item) -> None:
        """
        Remove all matching items from the bag.  If a bag contains
        {1, 4, 6, 6, 7}, removeall on 6 would result in a bag
        containing {1, 4, 7}.

        If removeall is called on an item not in the bag then this
        raises a KeyError.

        :param item: item to be removed.
        :return: None
        :raises KeyError: if item to be removed is not in the bag.
        """
        # removes all that match.
        if item not in self._contents:
                raise KeyError

        del self._contents[item]

    def discardall(self, item) -> None:
        """
        Discard all instances of item from the bag.

        An item is discarded if it equal according to the item's
        __eq__ method (i.e., the == operator).

        :param item: item to be removed
        :return: None
        """
        # discards all that match based on the == operator.
        if item not in self._contents:
                return

        del self._contents[item]

    def count(self, item) -> int:
        """
        Return the number of items matching the passed item in the bag.

        :param item:
        :return:
        """
        if item not in self._contents:
            return 0
        return self._contents[item]

    def __repr__(self) -> str:
        return "Bag({" + ", ".join([repr(i) for i in self]) + "})"


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import time
    import random

    def test():
        import matplotlib.pyplot as plt
        import time
        N = 1000
        add_run_times = []
        for n in range(1, N, 10):
            b = Bag()
            start_time = time.time()  # time in seconds
            for _ in range(n):
                b.add(random.randint(1, 10))
            end_time = time.time()
            add_run_times.append((end_time - start_time)/n)

        x = range(1, N, 10)
        plt.scatter(x, add_run_times, color="red")
        plt.title('Execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')
        plt.show()

    def main():
        # add some examples here.
        b = Bag([5,6,6])

        # run a performance test.
        N = 1000    # number of items to be inserted.
        M = 100     # repeat the test
        run_times = []

        for n in range(1, N):
            begin_time = time.time()

            for i in range(M):
                b = Bag()
                for j in range(1, n):
                    b.add(random.randint(1, 10))

            end_time = time.time()

            elapsed_time = end_time - begin_time
            run_times.append(elapsed_time/(n * M))

            print("%d total elapsed time: %f" % (n, elapsed_time))

        x = range(1,N)
        plt.scatter(x, run_times, color="blue")
        plt.title('Execution times')
        plt.xlabel('N')
        plt.ylabel('t (seconds)')

        plt.show()

    #main()
    test()