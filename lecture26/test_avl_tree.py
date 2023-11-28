import unittest
from lecture26.avl_tree import AVLTree


class TestAVLTree(unittest.TestCase):
    def test_init(self):
        t = AVLTree()
        self.assertEqual(0, len(t))

    def test_put(self):
        t = AVLTree()
        t.put(4, "foo")
        self.assertEqual(1, len(t))

    def test_find(self):
        t = AVLTree()
        try:
            t.find(7)
            self.assertTrue(False)  # shouldn't reach here.
        except KeyError:
            pass

        t.put(4, "foo")
        v = t.find(4)
        self.assertEqual("foo", v)

        t.put(6, "bar")
        v = t.find(4)
        self.assertEqual("foo", v)
        v = t.find(6)
        self.assertEqual("bar", v)
        try:
            t.find(7)
            self.assertTrue(False)  # shouldn't reach here.
        except KeyError:
            pass

        t.put(1, "goo")
        v = t.find(1)
        self.assertEqual("goo", v)

    def test_update_balance(self):
        t = AVLTree()
        t.put(8, "rooty")
        self.assertEqual(0, t._root.balance_factor)

        t.put(6, "lefty")
        self.assertEqual(1, t._root.balance_factor)
        self.assertEqual(0, t._root.left_child.balance_factor)

        t.put(9, "righty")
        self.assertEqual(0, t._root.balance_factor)
        self.assertEqual(0, t._root.left_child.balance_factor)
        self.assertEqual(0, t._root.right_child.balance_factor)

        t.put(10, "binrighty")
        self.assertEqual(-1, t._root.balance_factor)
        self.assertEqual(-1, t._root.right_child.balance_factor)
        self.assertEqual(0, t._root.right_child.right_child.balance_factor)
        self.assertEqual(0, t._root.left_child.balance_factor)

        t.put(4, "binlefty")
        self.assertEqual(0, t._root.balance_factor)
        self.assertEqual(1, t._root.left_child.balance_factor)
        self.assertEqual(0, t._root.left_child.left_child.balance_factor)
        self.assertEqual(-1, t._root.right_child.balance_factor)
        self.assertEqual(0, t._root.right_child.right_child.balance_factor)


    def test_left_rotation(self):
        t = AVLTree()
        t.put(6, "bar")
        t.put(8, "boo")
        t.put(9, "arggg")  # now needs left rotation.

        self.assertEqual(3, len(t))
        self.assertEqual(0, t._root.balance_factor)
        self.assertEqual(8, t._root.key)

    def test_right_rotation(self):
        t = AVLTree()
        t.put("c", "bar")
        self.assertEqual(0, t._root.balance_factor)
        t.put("b", "boo")
        self.assertEqual(1, t._root.balance_factor)
        t.put("a", "goo")  # now needs left rotation.

        self.assertEqual(3, len(t))
        self.assertEqual(0, t._root.balance_factor)
        self.assertEqual("b", t._root.key)
        self.assertEqual("a", t._root.left_child.key)
        self.assertEqual("c", t._root.right_child.key)

    def test_left_right_rotation(self):
        t = AVLTree()
        t.put("c", "caw")
        t.put("a", "ah")
        t.put("b", "baa")
        self.assertEqual(3, len(t))
        self.assertEqual(0, t._root.balance_factor)
        self.assertEqual("b", t._root.key)
        self.assertEqual("a", t._root.left_child.key)
        self.assertEqual("c", t._root.right_child.key)

    def test_right_left_rotation(self):
        t = AVLTree()
        t.put("a", "ah")
        t.put("c", "caw")
        t.put("b", "baa")
        self.assertEqual(3, len(t))
        self.assertEqual(0, t._root.balance_factor)
        self.assertEqual("b", t._root.key)
        self.assertEqual("a", t._root.left_child.key)
        self.assertEqual("c", t._root.right_child.key)


