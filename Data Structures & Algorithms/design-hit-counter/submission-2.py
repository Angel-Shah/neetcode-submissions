class HitCounter:

    def __init__(self):
        self.hitsQueue = []
        self.lowestTimestamp = float('inf')
        

    def hit(self, timestamp: int) -> None:
        self.hitsQueue.append(timestamp)
        self.lowestTimestamp = min(self.lowestTimestamp,timestamp)
        print(f"just got a hit, hitQueue:{self.hitsQueue}, lowestTimestamp:{self.lowestTimestamp}")

    def getHits(self, timestamp: int) -> int:
        begin = timestamp - 300

        l,r = 0,len(self.hitsQueue)-1

        while l <= r:
            mid = (l+r)//2
            if self.hitsQueue[mid] <= begin:
                l = mid +1
            else:
                r = mid -1
        print(f"getHits, mid:{mid}, returning:{self.hitsQueue[l:]}")
        return len(self.hitsQueue)-l
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
