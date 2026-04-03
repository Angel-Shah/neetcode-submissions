class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combs = []

        def helper(i,currComb,total):
            if total == target:
                    combs.append(currComb.copy())
                    return
            if total > target or i == len(candidates):
                return
            
            currComb.append(candidates[i])
            helper(i+1,currComb,total + candidates[i])
            currComb.pop()

            #while-loop to keep it moving until we get past duplicate nums
            while (i+1) <len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            helper(i+1,currComb,total)
        
        candidates.sort()
        helper(0,[],0)

        return combs