class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: 
                #in left arr
                if target < nums[l] or target > nums[mid]:
                    l = mid +1
                else:
                    r = mid -1
            else:
                #in right arr
                if target > nums[r] or target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
        return -1

       