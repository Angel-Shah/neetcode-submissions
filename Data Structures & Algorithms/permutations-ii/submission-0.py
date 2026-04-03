class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        uniquePerms = set()

        def helper(currPerm, picks):
            if len(currPerm) == len(nums):
                uniquePerms.add(tuple(currPerm))
                return
            
            for i in range(len(nums)):
                if not picks[i]:
                    currPerm.append(nums[i])
                    picks[i] = True
                    helper(currPerm,picks)
                    currPerm.pop()
                    picks[i] = False
        
        helper([],[False]*len(nums))
        return list(uniquePerms)