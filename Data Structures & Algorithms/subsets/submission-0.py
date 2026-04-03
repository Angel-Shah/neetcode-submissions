class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []

        def helper(i,currSet):
            if i == len(nums):
                subsets.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            #first include the nums[i]
            helper(i+1,currSet)

            #now remove, and don't inclue nums[i]
            currSet.pop()
            helper(i+1,currSet)
        
        helper(0,[])
        return subsets
            
        