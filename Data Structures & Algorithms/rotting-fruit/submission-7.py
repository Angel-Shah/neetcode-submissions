class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        queue = deque()
        visited = set()
       
        to_corrupt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    to_corrupt += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
   
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        time = 0

        while to_corrupt>0 and queue:
            for x in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if min(nr,nc)<0 or nr==rows or nc == cols or (nr,nc) in visited or grid[nr][nc]==0:
                        continue
                    grid[nr][nc] = 2
                    to_corrupt -= 1
                    queue.append((nr,nc))
                    visited.add((nr,nc))
            time +=1
        if to_corrupt ==0:
            return time
        else:
            return -1