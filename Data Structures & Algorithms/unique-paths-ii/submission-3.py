class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        dp[rows-1][cols-1] = 1
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = -1
                elif dp[r+1][c] == -1 and dp[r][c+1] == -1:
                    dp[r][c] == 0
                elif dp[r+1][c] == -1 and dp[r][c+1] != -1:
                    dp[r][c] += dp[r][c+1]
                elif dp[r+1][c] != -1 and dp[r][c+1] == -1:
                    dp[r][c] += dp[r+1][c]
                else:
                    dp[r][c] += (dp[r+1][c] + dp[r][c+1])

        if dp[0][0] == -1:
            return 0
        else:
            return dp[0][0]