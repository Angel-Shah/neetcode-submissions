class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prods = [1]*len(nums)
        suffix_prods = [1]*len(nums)
        print(prefix_prods)
        #fill out prefix first
        curr_prod = 1
        for i in range(1,len(nums)):
            curr_prod *= nums[i-1]
            prefix_prods[i] = curr_prod
        
        curr_prod = 1
        #now doing suffix array
        for i in range(len(nums)-2, -1, -1):
            curr_prod *= nums[i+1]
            suffix_prods[i] = curr_prod

        ans = []
        for i in range(len(nums)):
            ans.append(prefix_prods[i]*suffix_prods[i])

        return ans


