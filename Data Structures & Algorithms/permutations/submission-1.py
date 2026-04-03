class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def helper(currPerm, picks):
            if len(currPerm) == len(nums):
                permutations.append(currPerm.copy())
                return
            
            for i in range(len(nums)):
                if not picks[i]:
                    currPerm.append(nums[i])
                    picks[i] = True
                    helper(currPerm,picks)
                    currPerm.pop()
                    picks[i] = False
        
        helper([],[False]*len(nums))
        return permutations