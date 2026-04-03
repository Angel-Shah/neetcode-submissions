class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        rows,cols = len(grid),len(grid[0])
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while fresh > 0 and queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (min(nr,nc) >= 0 and nr < rows and nc < cols
                        and (nr,nc) not in visited and grid[nr][nc]==1):
                        fresh -= 1
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            time += 1
        if fresh == 0:
            return time
        else:
            return -1
