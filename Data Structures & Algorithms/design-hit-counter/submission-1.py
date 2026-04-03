class HitCounter:

    def __init__(self):
        self.hitsQueue = collections.deque()
        

    def hit(self, timestamp: int) -> None:
        self.hitsQueue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        begin = timestamp - 300 +1
        while self.hitsQueue:
            diff = timestamp - self.hitsQueue[0]
            if diff >= 300:
                self.hitsQueue.popleft()
            else:
                break
        return len(self.hitsQueue)

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
