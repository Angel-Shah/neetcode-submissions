class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in n_set:
                curr_longest = 0
                curr_val = num
                while curr_val in n_set:
                    curr_longest +=1
                    longest = max(longest,curr_longest)
                    curr_val += 1
        return longest
