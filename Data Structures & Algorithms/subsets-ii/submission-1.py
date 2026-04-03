class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def helper(i,currSet):
            if i == len(nums):
                subsets.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            helper(i+1,currSet)
            currSet.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1,currSet)
        
        helper(0,[])
        return subsets