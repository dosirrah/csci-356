
import unittest
from hw4.p4.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def test_init(self):
        hmap = HashTable()
        self.assertEqual(0, len(hmap))

    def test_put(self):
        hmap = HashTable()
        hmap.put(10, "foo")
        self.assertEqual(1, len(hmap))

        hmap.put( 23, "bar")
        self.assertEqual(2, len(hmap))

    def test_get(self):
        hmap = HashTable()
        hmap.put(10, "foo")
        v = hmap.get(10)
        self.assertEqual("foo", v)
        self.assertEqual(1, len(hmap))

        hmap.put(23, "bar")
        v = hmap.get(23)
        self.assertEqual("bar", v)
        self.assertEqual(2, len(hmap))

        self.assertIsNone(hmap.get(4))




