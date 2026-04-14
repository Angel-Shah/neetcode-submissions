class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start,end = 0,0
        windowSet = set([nums[0]])
        while end < len(nums): 
            if end-start == k:
                windowSet.remove(nums[start])
                start += 1

            end += 1
            if end < len(nums):
                if nums[end] in windowSet:
                        return True
                windowSet.add(nums[end])

        return False
