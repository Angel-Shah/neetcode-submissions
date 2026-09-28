class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid), len(grid[0])
        global_score = float('-inf')

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        minHeap = [(-grid[0][0],0,0)]

        while minHeap:
            path_min,r,c = heapq.heappop(minHeap)
            visited.add((r,c))
            path_min *= -1
            if (r,c) == (rows-1,cols-1):
                global_score = max(global_score,path_min)
                return global_score
            
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if min(nr,nc) >= 0 and nr < rows and nc < cols and (nr,nc) not in visited:
                    new_min = min(path_min,grid[nr][nc])
                    heapq.heappush(minHeap,(-new_min,nr,nc))