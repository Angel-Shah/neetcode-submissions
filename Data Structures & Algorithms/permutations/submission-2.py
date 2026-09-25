class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        # taken = set()

        def dfs(curr_permutation,curr_set):
            # print(f"currently: curr_permutation={curr_permutation}, curr_set = {curr_set}")
            if len(curr_permutation) == len(nums) :
                # print(f"appending:{curr_permutation}")
                ans.append(curr_permutation)
                return
            for val in curr_set:
                new_set = curr_set.copy()
                new_set.remove(val)
                # curr_permutation.append(val)
                new_permute = curr_permutation.copy()
                new_permute.append(val)
                dfs(new_permute,new_set)
                # curr_permutation.pop(-1)
            return
        
        dfs([],set(nums))

        return ans