class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None

    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        node = Node(key, value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dic[node.key]

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
