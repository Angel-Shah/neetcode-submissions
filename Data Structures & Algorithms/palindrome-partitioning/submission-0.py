class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        currPart = []

        def dfs(i,j):
            if j == len(s):
                if i == j:
                    palindromes.append(currPart.copy())
                return
            currStr = s[i:j+1]
            if currStr == currStr[::-1]:#if it is palindrome
                currPart.append(currStr)
                dfs(j+1,j+1)
                currPart.pop()
            
            #not a palindrome, so we recursive try to increase current region
            #in hopes it is palindrome
            dfs(i,j+1)
        
        dfs(0,0)

        return palindromes