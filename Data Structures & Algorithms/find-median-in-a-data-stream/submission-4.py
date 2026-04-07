class MedianFinder:

    def __init__(self):
        self.small = [] # max-heap
        self.large = [] # min-heap
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.small,-1*num) #push to small heap my default


        #now we correct
        if self.small and self.large and -1*self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if len(self.small) > len(self.large) + 1 :
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if len(self.large) > len(self.small) + 1 :
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)
        

    def findMedian(self) -> float:
        # print(f"FindMedian called: small:{self.small} , large:{self.large}")
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1*self.small[0]) + self.large[0])/2
        
        