from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            print(f"BEFORE: l:{l},r:{r},mid:{mid}")
            if (mid-1 >= 0 
                and mid+1 < len(nums) 
                and nums[mid] != nums[mid-1] 
                and nums[mid] != nums[mid+1]):
                return nums[mid]
            if nums[mid] == nums[mid-1]:
                if mid%2 == 1:
                    l = mid +1
                else:
                    r = mid -2
            if nums[mid] == nums[mid+1]:
                if mid%2 == 0:
                    l = mid +2
                else:
                    r = mid -1
            print(f"AFTER:  l:{l},r:{r},mid:{mid}")
            
        return nums[l]