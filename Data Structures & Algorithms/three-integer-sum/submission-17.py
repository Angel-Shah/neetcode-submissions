class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for idx, a in enumerate(nums):
            if idx > 0 and a == nums[idx-1]:
                continue
            l,r = idx+1, len(nums)-1
            while l < r:
                currSum = a + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                if currSum < 0:
                    l += 1
                if currSum == 0:
                    result.append([a,nums[l],nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
        return result