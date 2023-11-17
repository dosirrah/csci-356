
"""BinaryTree based on the binary tree implementation
provided by Miller and Ranum's *Problem Solving with Algorithms
and Data Structures using Python* section 7.6.

This is slightly modified to obey PEP 8 conventions.
"""
import sys


class BinaryTree:

    def __init__(self, key):
        self._key = key
        self._left_child = None
        self._right_child = None

    def insert_left(self, key):

        if self._left_child is None:
            self._left_child = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t._left_child = self._left_child
            self._left_child = t

    def insert_right(self, key):
        if self._right_child is None:
            self._right_child = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t._right_child = self._right_child
            self._right_child = t

    @property
    def right_child(self):
        # The book uses getRightChild, but this is not only
        # camelcase, which violates PEP 8 conventions, the
        # more accepted way is to implement a getter using
        # @property
        return self._right_child

    @property
    def left_child(self):
        # See the comment for right_child.
        return self._left_child

    @property
    def key(self):
        # The book uses get_root(), but it is convention
        # to use @property to create a getter.
        return self._key

    @key.setter
    def key(self, value):
        # The book uses set_root(value), but it is convention
        # to use a setter.
        self._key = value


def preorder(node: BinaryTree):
    if node is not None:
        sys.stdout.write(f" {node.key}")
        sys.stdout.flush()
        preorder(node.left_child)
        preorder(node.right_child)


def inorder(node: BinaryTree):
    if node is None:
        return
    inorder(node.left_child)
    sys.stdout.write(f" {node.key}")
    sys.stdout.flush()
    inorder(node.right_child)


def postorder(node: BinaryTree):
    if node is None:
        return
    postorder(node.left_child)
    postorder(node.right_child)
    sys.stdout.write(f" {node.key}")
    sys.stdout.flush()


if __name__ == "__main__":

    def main():
        # create tree
        #      6
        #     / \
        #    4   9
        #   / \
        #  1   5

        t = BinaryTree(6)
        t.insert_left(4)
        t.insert_right(9)
        ch = t.left_child
        ch.insert_left(1)
        ch.insert_right(5)

        print("in-order traversal:")
        inorder(t)

        print("\n\npre-order traversal")
        preorder(t)

        print("\n\npost-order traversal")
        postorder(t)

    main()
