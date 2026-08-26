from heapq import heappush,heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        heap = []
        heappush(heap,(grid[0][0],0,0))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        while heap:
            weight, r,c = heappop(heap)
            if r == rows-1 and c == cols-1:
                return weight
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if min(nr,nc)<0 or nr == rows or nc == cols or (nr,nc) in visited:
                    continue
                heappush(heap,(max(weight,grid[nr][nc]),nr,nc))
                visited.add((nr,nc))
