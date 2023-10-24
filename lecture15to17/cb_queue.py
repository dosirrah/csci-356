from __future__ import annotations
from circular_buffer import CircularBuffer

class CBQueue:
    """Implementation of a Queue based on a circular buffer."""

    def __init__(self):
        self._items = CircularBuffer()

    def enqueue(self, item):
        self._items.push_back(item)

    def dequeue(self):
        return self._items.pop_front()

    def __len__(self):
        return len(self._items)

    def reserve(self, capacity: int):
        self._items.reserve(capacity)
