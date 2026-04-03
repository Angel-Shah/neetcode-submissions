class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        while l<r:
            mid = (l+r)//2
            print(f"l:{l}, r:{r}, mid:{mid}")
            # if mid == l:
            #     return nums[r]
            # if mid == r:
            #     return nums[l]
            #this case means we are at the min:
            if nums[mid-1] > nums[mid] and nums[(mid+1)%len(nums)] > nums[mid]:
                return nums[mid]
            #already in a sorted segment, go left
            if nums[l] != nums[mid] and nums[mid] < nums[r]:
                r = mid - 1
            # elif nums[l] > nums[mid] and nums[mid] < nums[r]:
            #     r = mid - 1
            else:
                l = mid +1

        return nums[l]
