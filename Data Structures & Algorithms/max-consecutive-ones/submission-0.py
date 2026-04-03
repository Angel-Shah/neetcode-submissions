class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for n in nums:
            if n == 1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0
        return maxCount