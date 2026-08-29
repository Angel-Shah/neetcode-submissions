class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*(m+1) for i in range(n+1)]
        grid[n-1][m-1] = 1
        for i in range(len(grid)):
            print(grid[i])
        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                print
                grid[r][c] += grid[r+1][c] + grid[r][c+1]
        return grid[0][0]