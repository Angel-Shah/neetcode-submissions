import random
class RandomizedSet:

    def __init__(self):
        self.randSet = set()
        self.setLen = 0

    def insert(self, val: int) -> bool:
        if val not in self.randSet:
            self.randSet.add(val)
            self.setLen += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randSet:
            self.randSet.remove(val)
            self.setLen -= 1
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.randSet))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()