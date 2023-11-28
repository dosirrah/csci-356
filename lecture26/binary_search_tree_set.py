"""Binary search tree that only holds keys.

STL has both map and sets which underneath are both implemented
using binary trees.  Whether a tree stores keys or key-values
has identical time complexity for all operations.  It is merely
a matter of avoiding the constant memory and computation
to maintain unused value fields if we only want a set.
"""


class BinarySearchTreeSet:

    class _Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._len = 0

    def length(self):
        return self._len

    def __len__(self):
        return self._len

    def add(self, key):
        if self._root:
            self._put(self._root, key)
        else:
            self._root = BinarySearchTreeSet._Node(key)
        self._len += 1

    def _put(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BinarySearchTreeSet._Node(key)
            else:
                self._put(node.left, key)
        elif node.right is None:
            node.right = BinarySearchTreeSet._Node(key)

        else:
            self._put(node.right, key)

    def __contains__(self, key):
        def _find(n):
            if n is None:
                return False
            elif key == n.key:
                return True
            elif key < n.key:
                return _find(n.left)
            else:
                return _find(n.right)

        return _find(self._root)