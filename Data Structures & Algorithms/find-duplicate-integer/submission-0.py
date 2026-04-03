class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        # print(counts)
        for key,val in counts.items():
            if val > 1:
                return key