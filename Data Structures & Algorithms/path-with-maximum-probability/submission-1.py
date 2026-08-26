from heapq import heappush,heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = {i:[] for i in range(n)}
        for idx,edge in enumerate(edges):
            src,dst = edge[0],edge[1]
            adj_list[src].append([dst,succProb[idx]])
            adj_list[dst].append([src,succProb[idx]])

        max_probs = {}
        heap = []
        heappush(heap,(-1,start_node))
        while heap:
            prob,node = heappop(heap)
            prob*= -1
            if node == end_node:
                return prob
            if node in max_probs:
                continue
            max_probs[node] = prob

            for node2,prob2 in adj_list[node]:
                heappush(heap,(-(prob*prob2),node2))
        return 0