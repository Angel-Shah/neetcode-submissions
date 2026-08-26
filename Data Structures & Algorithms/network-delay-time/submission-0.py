from heapq import heappush,heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1,n+1)}
        for src,dst,w in times:
            adj_list[src].append([dst,w])
        
        #setup
        heap = []
        heappush(heap,(0,k))
       
        shortest_paths = {}
        min_time = float('-inf')

        while heap and len(shortest_paths) != n:
            weight,node = heappop(heap)
            # print(f"currently processing: <{weight},{node}>")
            if node in shortest_paths:
                continue
            shortest_paths[node] = weight
            min_time = max(min_time,weight)
            for n2,w2 in adj_list[node]:
                # print(f"pushing to heap: <{weight+w2},{n2}>")
                heappush(heap,(weight+w2,n2))
                # print(f"heap now look lik: {heap}")

        # print(f"min_time:{min_time}")
        # print(f"shortest_paths:{shortest_paths}")
        if len(shortest_paths) != n:
            return -1
        else:
            return min_time
