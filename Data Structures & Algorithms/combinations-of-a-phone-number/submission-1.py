class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        lookup = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        def helper(i,currSet):
            if i == len(digits):
                combinations.append(''.join(currSet))
                return
            
            # print(f"lookup[digits[i]]:{lookup[digits[i]]}")
            
            for c in lookup[digits[i]]:
                currSet.append(c)
                # print(f"currSet is :{currSet}")
                helper(i+1,currSet)
                currSet.pop()
        
        if digits:
            helper(0,[])
        return combinations