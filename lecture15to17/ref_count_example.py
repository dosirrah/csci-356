from __future__ import annotations  # allow Node to refer to Node in type hints.

def f():
    x = 10    # create PyObject '10' with reference count 1 via x.
              # x is referenced via the f_locals dict in the stack
              # frame for f.

    y = x     # reference count to '10' is 2.  1 from x and y from y.
              # both x and y are referenced from f_locals dict.

    return    # pops stack frame for f.
    # once f_locals for stack frame f ceases to exist, the reference
    # count to '10' goes to zero.
    # The PyObject holding '11' is deallocated.


class Node:
    def __init__(self, parent: Node):
        self._parent = parent
        self._children = []

    def add_child(self, child: Node):
        self._children.append(child)

def create_cycle():
    root = Node(None)
    child = Node(root)
    root.add_child(child)


create_cycle()