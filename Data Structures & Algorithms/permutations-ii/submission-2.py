class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        # print(counts)
        results = []
        def dfs(i, curr_num):
            if i == len(nums):
                results.append(curr_num)
                return
            
            for key,val in counts.items():
                if val > 0:
                    new_num = curr_num.copy()
                    new_num.append(key)
                    counts[key] -= 1
                    dfs(i+1,new_num)
                    counts[key] += 1

        dfs(0,[])
        return results