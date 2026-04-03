class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                neighbours = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in neighbours:
                    nr,nc = r + dr , c + dc
                    if ((min(nr,nc) < 0) 
                        or nr == rows 
                        or nc == cols
                        or (nr,nc) in visited 
                        or grid[nr][nc] == -1):
                        continue
                    queue.append((nr,nc))
                    visited.add((nr,nc))
                    grid[nr][nc] = distance + 1
            distance += 1
        