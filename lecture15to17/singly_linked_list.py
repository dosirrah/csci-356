"""
Contains an implementation of a singly-linked list.
"""

from __future__ import annotations

# Aside:
# In multiple places I use:
#
#   # noinspection PyProtectedMember
#
# This tells PyCharm to not generate any warnings for accessing protected
# members based on the Python convention of preceding protected members
# with an underscore.  However, when dealing with nested classes
# like _Node and _Iterator, these can be considered "part of" the
# SinglyLinkedList implementation.  As such, it is reasonbale that
# a nested class would access the protected members of its outer class.
#


class SinglyLinkedList:
    """Singly-linked list.  A singly linked list supports
       pushing to the back and popping from the front.  It
       does not support pushing and popping from both ends
       as is possible with a doubly-linked list.

       A doubly-linked list is required for HW3."""

    class _Node:
        def __init__(self, item: object):
            self._next = None
            self._item = item

    def __init__(self):
        """Constructor of the SinglyLinkedList."""
        self._front = None
        self._end = None
        self._n = 0

    def push_back(self, x) -> None:
        """Pushes the item x to the rear of the linked list."""
        if self._front is None:
            assert self._end is None
            node = SinglyLinkedList._Node(x)
            self._front = self._end = node
            self._n = 1
        else:
            node = SinglyLinkedList._Node(x)
            self._end._next = node
            self._end = node
            self._n += 1

    def __len__(self) -> int:
        """
        :return: number of items in the linked list.
        """
        return self._n

    def pop_front(self) -> object:
        """
        Removes first element from linked list and returns it.
        
        :return: removes and returns first element from the linked list. 
        :raises: IndexError if trying to pop from an empty linked list.
        """
        if self._n == 0:
            raise IndexError("Cannot pop from an empty linked list.")

        node = self._front
        # noinspection PyProtectedMember
        self._front = node._next
        if self._front is None:
            self._end = None

        # noinspection PyProtectedMember
        item = node._item
        self._n -= 1
        del node
        return item

