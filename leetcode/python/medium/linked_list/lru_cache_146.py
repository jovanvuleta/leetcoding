import collections


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    """
        Intuition: Hash map that represents a cache, in the map values are the nodes themselves
         that are linked together. We maintain two nodes: left and right.
         Left node - represents LRU
         Right node - represents MRU - most recently used
         By accessing/putting/going over the capacity insertion, we remove the node by de-referencing it, and adding
         it next to the dummy right node. By doing this we are able to access the LRU and MRU in constant time.
        Time complexity of get and put methods: O(1)
        Space complexity: O(N)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # map the key to nodes

        # left = LRU, right = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left  # link them together

    # remove node from list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # insert node at right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


class LRUCacheWithOrderedDict:
    """
        Intuition: Using ordered dict which keeps track of inserted keys and has option to move the key all the way to
        the right and also pop the first item from left (self.key_value.popitem(last=False)).
        Time complexity of get and put methods: O(1)
        Space complexity: O(N)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.key_value:
            self.key_value.move_to_end(key)
            return self.key_value[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_value:
            self.key_value.move_to_end(key)

        self.key_value[key] = value

        if len(self.key_value) > self.capacity:
            self.key_value.popitem(last=False)
