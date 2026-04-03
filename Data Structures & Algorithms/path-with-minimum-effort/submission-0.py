class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights),len(heights[0])
        shortest = {}
        minHeap = [(0,[0,0])]

        while minHeap:
            w,coord = heapq.heappop(minHeap)
            x,y = coord[0],coord[1]
            if (x,y) in shortest:
                continue
            shortest[(x,y)] = w
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                if (nx >= 0 and 
                    nx < rows and
                    ny >= 0 and
                    ny < cols
                    and (nx,ny) not in shortest):
                    abs_diff = abs(heights[x][y] - heights[nx][ny])
                    heapq.heappush(minHeap,(max(w,abs_diff),[nx,ny]))
        # print(shortest)
        return shortest[(rows-1,cols-1)]