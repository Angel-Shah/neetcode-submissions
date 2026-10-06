class Solution:
    def helper(self,nums):
        dp2 = dp1 = 0
        for n in nums:
            new_dp = max(dp2+n,dp1)
            dp2 = dp1
            dp1 = new_dp
        return dp1

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))