class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
            # if nums[mid-1] > nums[mid] and nums[(mid+1)%len(nums)] > nums[mid]:
            #     return nums[mid]
            # if nums[l] != nums[mid] and nums[mid] < nums[r]:
            #     r = mid - 1
            # else:
            #     l = mid +1

        return nums[r]
