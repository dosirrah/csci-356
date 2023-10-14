"""
Based on the implementation from *Problem Solving with Algorithms
and Data Structures using Python*.  I changed a few things
to be more inline with PEP 8 style guidelines.

https://runestone.academy/ns/books/published/pythonds/BasicDS/ImplementingaQueueinPython.html
"""


class ListQueue:
    """Implementation of a Queue based on Python's list."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # O(n) operation.
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)
