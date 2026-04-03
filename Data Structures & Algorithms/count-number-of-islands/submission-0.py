class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visited = set()
        islandCount = 0

        def dfs(nr,nc):
            if (
                nr >= 0 and
                nr < rows and
                nc >= 0 and
                nc < cols and
                (nr,nc) not in visited and
                grid[nr][nc] == '1'
            ):
                visited.add((nr,nc))
                #run dfs on up,down,left,right
                dfs(nr-1,nc)
                dfs(nr+1,nc)
                dfs(nr,nc-1)
                dfs(nr,nc+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islandCount += 1
                    dfs(r,c)
        return islandCount
                    
        