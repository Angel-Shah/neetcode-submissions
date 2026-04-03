class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0)+1
        print(counts)
        
        permutations = []
        currPerm = []
        def dfs():
            if len(currPerm) == len(nums):
                permutations.append(currPerm.copy())
                return
            
            for c in counts:
                if counts[c] > 0:
                    counts[c] -= 1
                    currPerm.append(c)
                    dfs()
                    counts[c] += 1
                    currPerm.pop()
        
        dfs()

        return permutations