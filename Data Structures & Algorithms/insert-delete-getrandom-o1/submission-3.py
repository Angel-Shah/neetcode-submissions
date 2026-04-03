import random
class RandomizedSet:

    def __init__(self):
        self.numList = []
        self.numHash = {}

    def insert(self, val: int) -> bool:
        if val not in self.numHash:
            self.numHash[val] = len(self.numList)
            self.numList.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.numHash:

            lastVal = self.numList[-1]
            idx = self.numHash[val]
            self.numList[idx] = lastVal
            self.numHash[lastVal] = idx
            self.numList.pop()
            del self.numHash[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()