class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        max_area = 0

        def dfs(r,c,grid):
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0 
            grid[r][c] = 0
            area = 1
            area += dfs(r-1,c,grid)
            area += dfs(r+1,c,grid)
            area += dfs(r,c-1,grid)
            area += dfs(r,c+1,grid)
            return area
         

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    print(f"found an island at ;{r},{c}")
                    island_area = dfs(r,c,grid)
                    max_area = max(max_area,island_area)
        return max_area