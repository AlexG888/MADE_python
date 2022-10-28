import logging
import logging.config


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if type(capacity) != int:
            logger.warning("LRUCache object accepts only integer as input")
        else:
            self.capacity = capacity
            self.dic = dict()
            self.head = Node(0, 0)
            self.tail = Node(0, 0)
            self.head.next = self.tail
            self.tail.prev = self.head
            logger.debug(f"initialized object LRUCache with capacity {capacity}")

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            logger.debug(
                f"node with key {key} and value {node.value} was recently used"
            )
            return node.value
        logger.debug(f"the node with the key {key} is not in the dictionary")
        return None

    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
            logger.debug(f"the node with the key {key} deleted from dictionary")
        node = Node(key, value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dic[node.key]
            logger.debug(f"the node with the key {node.key} deleted from dictionary")
        logger.debug(
            f"the node with the key {key} and value {node.value} added to dictionary"
        )

    def _add(self, node):
        n_prev = self.tail.prev
        n_prev.next = node
        self.tail.prev = node
        node.prev = n_prev
        node.next = self.tail

    def _remove(self, node):
        n_prev = node.prev
        n_next = node.next
        n_prev.next = n_next
        n_next.prev = n_prev


log_conf = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s\t%(levelname)s\t%(message)s",
        },
        "processed": {
            "format": "%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s",
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "cache.log",
            "formatter": "processed",
        },
        "stream_handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["file_handler", "stream_handler"],
        },
    },
}

logging.config.dictConfig(log_conf)
logger = logging.getLogger()


my_lru = LRUCache(2)
my_lru.set("k1", "val1")
my_lru.set("k2", "val2")
my_lru.get("k2")
my_lru.get("k1")
my_lru.set("k3", "val3")

my_lru = LRUCache(1)
my_lru.set("k1", "val1")
my_lru.set("k2", "val2")
my_lru.get("k2")
my_lru.get("k1")
my_lru.set("k3", "val3")

my_lru = LRUCache("a")
