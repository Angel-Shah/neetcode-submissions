from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # Ensure mid is at the start of a pair
            if mid % 2 == 1:
                mid -= 1
            
            # Check if we found the single element
            if nums[mid] != nums[mid + 1]:
                r = mid  # Single element is in left half
            else:
                l = mid + 2  # Single element is in right half
        
        return nums[l]