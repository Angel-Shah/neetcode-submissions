from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                xi,yi = points[i][0],points[i][1]
                xj,yj = points[j][0],points[j][1]
                man_dist = abs(xi-xj)+abs(yi-yj)
                adj_list[i].append([j,man_dist])
                adj_list[j].append([i,man_dist])
        
        mst_cost = 0
        heap = []
        visited = set()
        #initializing the heap with point 0
        for nei,dist in adj_list[0]:
            heappush(heap,(dist,0,nei))
        visited.add(0)
        
        while len(visited) < len(points):
            dist,src,dst = heappop(heap)
            if dst in visited:
                continue
            mst_cost += dist
            visited.add(dst)
            for nei,dist2 in adj_list[dst]:
                if nei not in visited:
                    heappush(heap,(dist2,dst,nei))

        return mst_cost