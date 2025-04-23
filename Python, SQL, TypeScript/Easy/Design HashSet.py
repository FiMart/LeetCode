class MyHashSet:

    def __init__(self):
        self.data = [False] * 1000001  # Initialize a list of size 1000001 with all values set to False

    def add(self, key: int) -> None:
        self.data[key] = True  # Set the value at index 'key' to True, indicating that the key is present in the set

    def remove(self, key: int) -> None:
        self.data[key] = False  # Set the value at index 'key' to False, indicating that the key is removed from the set

    def contains(self, key: int) -> bool:
        return self.data[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)