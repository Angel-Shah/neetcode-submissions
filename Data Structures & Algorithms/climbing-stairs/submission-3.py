class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0,1,2]
        if n<=2:
            return n
        for i in range(3,n+1):
            num_ways = dp[i-1] + dp[i-2]
            dp.append(num_ways)
        
        return dp[n]