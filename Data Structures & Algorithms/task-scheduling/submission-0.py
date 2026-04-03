import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqCount = {}
        for task in tasks:
            freqCount[task] = freqCount.get(task,0)+1

        heap = [-val for key,val in freqCount.items()]
        heapq.heapify(heap)

        time = 0

        queue = deque()

        while heap or queue:
            time += 1
            if heap:
                currMax = heapq.heappop(heap)
                if currMax + 1 != 0:
                    queue.append((currMax+1,time+n))

            while queue and queue[0][1] == time:
                val,time = queue.popleft()
                heapq.heappush(heap,val)

        return time