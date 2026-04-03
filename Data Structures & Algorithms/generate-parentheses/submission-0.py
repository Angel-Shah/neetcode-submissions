class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        permutations = []
        if n == 0:
            return permutations

        openings, closings = n,n

        def helper(currString, openingsUsed, closingsUsed):
            if openingsUsed > n or closingsUsed > openingsUsed:
                return
            if openingsUsed == n and closingsUsed == n:
                permutations.append(currString[:])
                return
            
            helper(currString+'(',openingsUsed +1, closingsUsed)
            helper(currString+')',openingsUsed , closingsUsed+1)

        helper("",0,0)

        return permutations

