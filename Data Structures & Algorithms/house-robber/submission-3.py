class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,0]
        for idx,num in enumerate(nums):
            rel_idx = idx+2
            dp.append(max(dp[rel_idx - 2]+num, dp[rel_idx - 1]))
        return dp[-1]

                
