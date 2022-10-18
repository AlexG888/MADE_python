import unittest
from lru import LRUCache


class TestLru(unittest.TestCase):
    def setUp(self):
        self.lru = LRUCache(2)

    def test_get(self):
        self.assertEqual(None, self.lru.get("k1"))

        self.lru.set("k1", "val1")
        self.lru.set("k2", "val2")
        self.assertIsNone(self.lru.get("k3"))
        self.assertEqual(self.lru.get("k2"), "val2")
        self.assertEqual(self.lru.get("k1"), "val1")

    def test_set(self):
        self.lru.set("k1", "val1")
        self.lru.set("k2", "val2")
        self.lru.get("k2")
        self.lru.get("k1")
        self.lru.set("k3", "val3")
        self.assertEqual(self.lru.get("k3"), "val3")
        self.assertIsNone(self.lru.get("k2"))
        self.assertEqual(self.lru.get("k1"), "val1")

        self.lru.set("k3", "val5")
        self.assertEqual(self.lru.get("k3"), "val5")
        self.lru.set("k1", "val1")
        self.lru.set("k2", "val2")
        self.assertIsNone(self.lru.get("k3"))

        self.assertEqual(len(self.lru.dic), 2)

        self.lru = LRUCache(1)
        self.lru.set("k1", "val1")
        self.assertEqual(self.lru.get("k1"), "val1")
        self.lru.set("k2", "val2")
        self.assertIsNone(self.lru.get("k1"))
        self.assertEqual(self.lru.get("k2"), "val2")
        self.assertEqual(len(self.lru.dic), 1)
