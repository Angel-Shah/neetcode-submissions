class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        maxRob = [nums[0],max(nums[0],nums[1])]

        for i in range(2,len(nums)):
            maxRob.append(max(maxRob[i-1],(nums[i]+maxRob[i-2])))

        return maxRob[-1]