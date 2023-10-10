"""
This module is based on the Stack class in Section 4.5 of
*Problem Solving with Algorithms and Data Structures using Python*.

https://runestone.academy/ns/books/published/pythonds/BasicDS/ImplementingaStackinPython.html
"""

class Stack:
    """Stack implementation based on chapter 4 from """

    def __init__(self):
        self.items = []

    def is_empty(self):  # was isEmpty in book, but PEP 8 conventions suggest snake case.
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
