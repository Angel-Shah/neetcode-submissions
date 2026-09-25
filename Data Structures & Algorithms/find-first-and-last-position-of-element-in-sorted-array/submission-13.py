import bisect
class Solution:
    def binarySearch(self,nums,target):
        l,r = 0,len(nums)
        while l < r:
            mid = (l+r)//2
            if target <= nums[mid]:
                r = mid
            else:
                l = mid +1
        return l
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums,target)
        print(f"left:{left}")
        if left == len(nums) or nums[left]!= target:
            return [-1,-1]
        else:
            right = self.binarySearch(nums,target+1)
            # while right < len(nums) and nums[right] == nums[left]:
            #     right += 1
            return [left,right-1]