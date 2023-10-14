from circular_buffer import CircularBuffer

class CBQueue:
    """Implementation of a Queue based on Python's list."""

    def __init__(self):
        self._items = CircularBuffer()

    def enqueue(self, item):
        # O(n) operation.
        self._items.push_back(item)

    def dequeue(self):
        return self._items.pop_front()

    def __len__(self):
        return len(self._items)
