class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        dirs = [[0,1],[1,0],[0,-1],[-1,0],[-1,-1],[-1,1],[1,1],[1,-1]]
        queue = deque()
        visited = set()
        shortest_path = 1

        queue.append((0,0))
        visited.add((0,0))


        while queue:
            for x in range(len(queue)):
                r,c = queue.popleft()
                if r == rows-1 and c == cols-1:
                    return shortest_path
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc]==0:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            shortest_path += 1

        return -1