class MyHashSet:

    def __init__(self):
        self.the_set = []

    def add(self, key: int) -> None:
        if key in self.the_set:
            return
        self.the_set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.the_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.the_set

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
