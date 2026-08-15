class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0,0]
        for i in range(2,len(cost)+1):
            minCost.append(min(cost[i-1]+minCost[i-1],cost[i-2]+minCost[i-2]))
        print(minCost)
        return minCost[-1]