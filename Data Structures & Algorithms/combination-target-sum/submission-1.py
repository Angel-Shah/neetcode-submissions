class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        subsets = []
  
        def helper(i,currSet,currSum):
            if currSum == target:
                subsets.append(currSet.copy())
                return
            if i == len(nums) or currSum > target:
                return
            
            #first we include current value
            currSet.append(nums[i])
            helper(i,currSet,currSum+nums[i])

            #now we want to not include this value and see
            currSet.pop()
            helper(i+1,currSet,currSum)

            
        
        helper(0,[],0)

        return subsets
