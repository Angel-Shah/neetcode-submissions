class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def helper(i,currSet):
            if len(currSet) == k:
                combs.append(currSet.copy())
                return
            if i > n:
                return
            
            currSet.append(i)
            helper(i+1,currSet)

            currSet.pop()
            helper(i+1,currSet)

        helper(1,[])
        return combs