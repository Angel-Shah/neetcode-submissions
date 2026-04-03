class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n_dict = {}
        for num in nums:
            n_dict[num] = False

        longest = 1
        for key,val in n_dict.items():
            if val == True:
                continue
            curr_longest = 1
            curr_val = key +1
            while curr_val in n_dict:
                curr_longest +=1
                longest = max(longest,curr_longest)
                n_dict[curr_val] = True
                curr_val += 1
        return longest
