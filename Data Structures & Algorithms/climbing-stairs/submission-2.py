class Solution:
    def climbStairs(self, n: int) -> int:
        #so since you can take either 1 step or 2 steps at a time,
        #our base cases are that for n =1 , ans = 1 and for n = 2, ans = 2
        numWays = [0,1,2]
        
        if n <= 2:
            return numWays[n]
        for i in range(3,n+1):
            numWays.append(numWays[i-1]+numWays[i-2])
        return numWays[n]