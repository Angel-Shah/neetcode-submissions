class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n_dict = {}
        for num in nums:
            n_dict[num] = num+1

        longest = 1
        for key,val in n_dict.items():
            curr_longest = 1
            curr_val = val
            while curr_val in n_dict:
                curr_longest +=1
                longest = max(longest,curr_longest)
                curr_val = n_dict[curr_val]
        return longest
