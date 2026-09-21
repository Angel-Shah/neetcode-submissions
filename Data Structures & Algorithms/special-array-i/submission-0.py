class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <=1:
            return True
        
        looking_odd = nums[0]%2
        looking_odd = not looking_odd
        
        for i in range(1,len(nums)):
            if looking_odd != nums[i]%2:
                print(f"at i={i}, looking_odd:{looking_odd}")
                return False
            looking_odd = not looking_odd
        return True