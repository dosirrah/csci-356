"""
Queue class copied from Listing 1 of

    https://runestone.academy/ns/books/published/pythonds/BasicDS/ImplementingaQueueinPython.html

I slightly modified the class to match PEP 8 conventions.
"""

class Queue:
    """
    A Queue implemented by wrapping a Python list.

    """

    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:   # renamed to be compliant with PEP 8 conventions.
        """
        :return: whether the Queue is empty.
        """
        return self.items == []

    def enqueue(self, item) -> None:
        """
        Enqueue the passed item to the end of the queue.

        :param item: item to be enqueued.
        :return: None
        """
        self.items.insert(0,item)

    def dequeue(self) -> object:
        """
        Remove the first item in the queue.
        :return: the item removed from the front of the queue.
        :raises IndexError: if the Queue is empty when dequeue is called.
        """
        return self.items.pop()

    def __len__(self):   # renamed size() to __len__ to match Python container conventions.
        """
        :return: the number of items in the Queue.
        """
        return len(self.items)