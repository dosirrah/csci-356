"""
This module is based on the Stack class in Section 4.5 of
*Problem Solving with Algorithms and Data Structures using Python*.

https://runestone.academy/ns/books/published/pythonds/BasicDS/ImplementingaStackinPython.html
"""

from linked_list import LinkedList

class LinkedListStack:
    """
    Stack implementation based on chapter 4 from
    *Problem Solving with Algorithms and Data Structures using Python*, and then
    modified to use the doubly-linked list class in linked_list.py.
    """

    def __init__(self):
        self._items = LinkedList()


    def is_empty(self):  # was isEmpty in book, but PEP 8 conventions suggest snake case.
        """
        :return: true iff the stack has no items.
        """
        return len(self._items) == 0


    def push(self, item: object):
        """
        :param item: item to be pushed to the top of the stack.
        :return: None
        """
        self._items.push_back(item)


    def pop(self):
        """
        :return: remove and then return the top item from the stack.
        :raises: IndexError if the stack is empty.
        """
        return self._items.pop_back()

    def peek(self):
        return self._items.peek_back()


    def __len__(self):  # was called size() in Python book.
        return len(self._items)