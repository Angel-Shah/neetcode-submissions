class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.vals_to_idx = {}


    def insert(self, val: int) -> bool:
        if val in self.vals_to_idx:
            return False
        self.vals_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals_to_idx:
            return False
        last_val = self.vals[-1]
        idx_replace = self.vals_to_idx[val]
        self.vals[idx_replace] = last_val
        self.vals.pop()
        self.vals_to_idx[last_val] = idx_replace
        del self.vals_to_idx[val]
        return True

    def getRandom(self) -> int:
        idx = random.randint(0,len(self.vals)-1)
        return self.vals[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()