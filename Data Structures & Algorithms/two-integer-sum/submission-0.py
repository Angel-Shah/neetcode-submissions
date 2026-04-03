class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       remainders = {}
       for idx,val in enumerate(nums):
            remain = target - val
            if val in remainders:
                return [remainders[val],idx]
            remainders[remain] = idx
        
        
        




