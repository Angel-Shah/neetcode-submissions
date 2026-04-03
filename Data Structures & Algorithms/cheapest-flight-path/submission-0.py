class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = {}
        for i in range(n):
            adj[i] = []

        for source,destination,cost in flights:
            adj[source].append([cost,destination])

        minCost = float('inf')
        queue = [[0,src]]   
        curr_stops = -1


        while queue:
            # print(f"queue:{queue}, curr_stops:{curr_stops}")
            new_queue = []
            if curr_stops > k:
                break
            for c,d in queue:
                if d == dst:
                    minCost = min(minCost,c)
                    # print(f"FOUND path that costs:{c}, with stops:{curr_stops}")
                for c2,d2 in adj[d]:
                    new_queue.append([c + c2, d2])
            curr_stops += 1
            queue = new_queue


        if minCost != float('inf'):
            return minCost
        else:
            return -1