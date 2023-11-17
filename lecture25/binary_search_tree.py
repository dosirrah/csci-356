class BinarySearchTree:

    class _Node:
        def __init__(self, key, val):
            self.key = key
            self.value = val
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._len = 0

    def length(self):
        return self._len

    def __len__(self):
        return self._len

    # def __iter__(self):
    #     return self._root.__iter__()

    def put(self, key, val):
        if self._root:
            self._put(self._root, key, val)
        else:
            self._root = BinarySearchTree._Node(key, val)
        self._len += 1

    def _put(self, node, key, val):
        if key < node.key:
            if node.left is None:
                node.left = BinarySearchTree._Node(key, val)
            else:
                self._put(node.left, key, val)
        elif node.right is None:
            node.right = BinarySearchTree._Node(key, val)

        else:
            self._put(node.right, key, val)

    def find(self, key):
        def _find(n):
            if n is None:
                raise KeyError
            elif key == n.key:
                return n.value
            elif key < n.key:
                return _find(n.left)
            else:
                return _find(n.right)

        return _find(self._root)