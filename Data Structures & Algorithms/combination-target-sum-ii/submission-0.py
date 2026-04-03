class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combs = []

        def helper(i,currComb):
            if sum(currComb) == target:
                    combs.append(currComb.copy())
                    return
            if i==len(candidates):
                return
            
            currComb.append(candidates[i])
            helper(i+1,currComb)
            currComb.pop()

            #while-loop to keep it moving until we get past duplicate nums
            while (i+1) <len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            helper(i+1,currComb)
            # for j in range(i,len(candidates)):
            #     currComb.append(candidates[j])
            #     helper(j+1,currComb)
            #     currComb.pop()
        
        candidates.sort()
        helper(0,[])

        return combs