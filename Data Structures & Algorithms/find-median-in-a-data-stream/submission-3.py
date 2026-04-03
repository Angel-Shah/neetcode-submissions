

class MedianFinder:

    def __init__(self):
        self.left = [] #max-heap
        self.right = [] #min-heap
        

    def addNum(self, num: int) -> None:
        #by default start by adding to the left max heap
        heapq.heappush(self.left,-1 * num)
        #check if max-left is > min-right
        if (self.left and self.right 
            and (-1*self.left[0]) > self.right[0]):
            val = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right,val)
        
        #balance size diff from left/right
        if len(self.left) > len(self.right) + 1: #left is bigger
            val = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right,val)
        if len(self.right) > len(self.left) + 1: #right is bigger
            val = heapq.heappop(self.right)
            heapq.heappush(self.left,-1*val)

    def findMedian(self) -> float:
        #if left is bigger
        if len(self.left) > len(self.right):
            return -1* self.left[0]

        #if right is bigger
        if len(self.right) > len(self.left):
            return self.right[0]

        #if they are the same length, take mean of mid vals
        return ((-1* self.left[0]) + self.right[0])/2


        