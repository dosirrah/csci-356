
from __future__ import annotations


class LinkedList:
    """Doubly-linked list."""

    class _Node:
        def __init__(self, prev: LinkedList._Node | None,
                     next: LinkedList._Node | None, item: object):
            self._prev = prev
            self._next = next
            self._item = item

    class _Iterator:
        def __init__(self, linked_list: LinkedList):
            self._i = linked_list._front

        def __iter__(self):
            return self

        def __next__(self) -> object:
            if self._i is None:
                raise StopIteration

            item = self._i._item
            self._i = self._i._next
            return item

    def __init__(self):
        self._front = None
        self._end = None
        self._n = 0

    def __iter__(self):
        return LinkedList._Iterator(self)

    def push_back(self, x) -> None:
        """Pushes the item x to the rear of the linked list."""
        if self._front is None:
            assert self._end is None
            node = LinkedList._Node(None, None, x)
            self._front = self._end = node
            self._n = 1
        else:
            node = LinkedList._Node(self._end, None, x)
            self._end._next = node
            self._end = node
            self._n += 1

    def push_front(self, x) -> None:
        """Pushes the item x to the front of the linked list."""
        if self._front is None:
            assert self._end is None
            node = LinkedList._Node(None, None, x)
            self._front = self._end = node
            self._n = 1
        else:
            node = LinkedList._Node(None, self._front, x)
            self._front._prev = node
            self._front = node
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
        if self._front is not None:
            self._front.prev = None
        else:
            self._end = None

        # noinspection PyProtectedMember
        item = node._item
        self._n -= 1
        del node
        return item

    def pop_back(self) -> object:
        """
        Removes and then returns the last item in the linked list.
        :return: removes and then returns the last item in the linked list.
        :raises: IndexError if trying to pop from an empty linked list.
        """
        if self._n == 0:
            raise IndexError("Cannot pop from an empty linked list.")

        node = self._end
        # noinspection PyProtectedMember
        self._end = node._prev
        if self._end is not None:
            self._end._next = None
        else:
            self._front = None

        # noinspection PyProtectedMember
        item = node._item
        self._n -= 1

        del node
        return item

    def peek_back(self):
        """
        :return: the last item in the linked list without modifying the linked list.
        """
        if self._n == 0:
            raise IndexError("Cannot peek into an empty linked list.")

        # noinspection PyProtectedMember
        return self._end._item

    def peek_front(self):
        """
        :return the first tiem in the linked list without modiyfing the linkedlist.
        """
        if self._n == 0:
            raise IndexError("Cannot peek into an empty linked list.")

        # noinspection PyProtectedMember
        return self._front._item
