class Solution:

    def __init__(self, w: List[int]):
        self.rangeSum = -1
        self.ranges = []
        for weight in w:
            self.rangeSum += weight
            self.ranges.append(self.rangeSum)
        
        

    def pickIndex(self) -> int:
        randVal = random.randint(0,self.rangeSum)
        l,r = 0, len(self.ranges)-1
        while l < r:
            mid = (l+r)//2
            if randVal > self.ranges[mid]:
                l = mid +1
            else:
                r = mid
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()