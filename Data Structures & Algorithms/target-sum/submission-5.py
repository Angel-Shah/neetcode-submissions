class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        num_ways = 0

        cache = {}

        def dfs(i,curr_sum):
            if (i,curr_sum) in cache:
                return cache[(i,curr_sum)]
            if i==len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
           
            cache[(i,curr_sum)] = dfs(i+1,curr_sum + nums[i]) + dfs(i+1,curr_sum - nums[i])
            return cache[(i,curr_sum)]

        return dfs(0,0)