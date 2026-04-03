from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        for key,val in numCount.items():
            if val == 1:
                return key