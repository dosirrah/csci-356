# The rest of this bag will be implemented in class on Thursday, Sept 7.
# This is a skeleton created alongside the tests in test_bag.py

from collections import defaultdict

class Bag:

    def __init__(self):
        self._contents = defaultdict(int)

    def __len__(self):   # if x is a Bag __len__ called when len(x)
        return 0

    def __contains__(self) -> bool: # if x is a Bag __contains__ called with "in"
        return False

    def add(self, item):
        self._contents[item] += 1

    def remove(self, item):
        pass
