class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums =set()
        last_added_idx = 0
        new_arr = []
        for idx,n in enumerate(nums):
            if n not in set_nums:
                set_nums.add(n)
                last_added_idx = idx
                new_arr.append(n)
        
        for idx,val in enumerate(new_arr):
            nums[idx] = new_arr[idx]

        return len(new_arr)
