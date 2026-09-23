class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
            return [-1,-1]
        
        l,r = 0,len(nums)-1
        candidate = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target:
                if nums[mid] == target:
                    candidate = mid
                r = mid-1
            else:
                l = mid +1
        
        # print(f"l:{l},r:{r}, value at l:{nums[l]}")
        # print(f"candidate:{candidate}, value at candidate:{nums[candidate]}")
        if l > r and candidate == -1:
            return [-1,-1]
        end = l
        while end < len(nums) and nums[end] == nums[l]:
            end += 1
        
        return [l,end-1]