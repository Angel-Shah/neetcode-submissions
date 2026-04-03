class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for n in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap,n)
            else:
                if n >= self.heap[0]:
                    heapq.heappush(self.heap,n)
                    heapq.heappop(self.heap)

        print(f"after initialization heap:{self.heap}")
        self.k = k
        

    def add(self, val: int) -> int:
       
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            print(f"len<k ,added {val} to heap: {self.heap}, will return:{self.heap[0]}")
            return self.heap[0]
        else:
            if val >= self.heap[0]:
                heapq.heappush(self.heap,val)
                retVal = heapq.heappop(self.heap)
                print(f"len = k, added {val} to heap: {self.heap}, will return:{self.heap[0]}")
            return self.heap[0] 