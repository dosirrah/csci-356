"""
An SSLQueue is a queue based on a singly-linked list.
"""

from lecture15to17.singly_linked_list import SinglyLinkedList


class SLLQueue:
    """Implementation of a Queue based on Python's list."""

    def __init__(self):
        self._items = SinglyLinkedList()

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        # O(n) operation.
        self._items.push_back(item)

    def dequeue(self):
        return self._items.pop_front()

    def __len__(self):
        return len(self._items)
