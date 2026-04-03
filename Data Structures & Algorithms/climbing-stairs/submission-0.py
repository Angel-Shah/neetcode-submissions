class Solution:
    def climbStairs(self, n: int) -> int:
        #so since you can take either 1 step or 2 steps at a time,
        #our base cases are that for n =1 , ans = 1 and for n = 2, ans = 2
        if n <= 2:
            return n    
        dp = [1,2]
        i = 3
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1
        return dp[1]