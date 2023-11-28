from __future__ import annotations


class AVLTree:
    class TreeNode:
        def __init__(self, key, val, parent):
            self.key = key
            self.val = val
            self.parent = parent
            self.left_child = None
            self.right_child = None
            self.balance_factor = 0

        def has_right_child(self) -> bool:
            return self.right_child is not None

        def has_left_child(self) -> bool:
            return self.left_child is not None

        def is_left_child(self) -> bool:
            return self.parent.left_child == self

        def is_right_child(self) -> bool:
            return self.parent.right_child == self

        def is_root(self) -> bool:
            return self.parent is None

    def __init__(self):
        self._root = None
        self._len = 0

    def __len__(self):
        return self._len

    def put(self, key, val):
        if self._root is None:
            self._root = AVLTree.TreeNode(key, val, None)
        else:
            self._put(key, val, self._root)
        self._len += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = \
                    AVLTree.TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = \
                    AVLTree.TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node: AVLTree.TreeNode):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self,node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)


    def rotate_left(self, rot_root):
        new_root = rot_root.right_child
        rot_root.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self._root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root
        new_root.left_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)


    def rotate_right(self, rot_root):
        new_root = rot_root.left_child
        rot_root.left_child = new_root.right_child
        if new_root.right_child is not None:
            new_root.right_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self._root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right_child = new_root
            else:
                rot_root.parent.left_child = new_root
        new_root.right_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor - 1 + max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 - min(rot_root.balance_factor, 0)

        # rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        # new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)


    def find(self, key):
        def _find(n):
            if n is None:
                raise KeyError
            elif key == n.key:
                return n.val
            elif key < n.key:
                return _find(n.left_child)
            else:
                return _find(n.right_child)

        return _find(self._root)