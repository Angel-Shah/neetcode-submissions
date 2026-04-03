class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]

        dp[0][0] = True #when no string and no pattern it is matching

        for j in range(1,len(dp[0])):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                # matches characters
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                #no match
                elif p[j-1] == '*':
                    #zero
                    dp[i][j] = dp[i][j-2]

                    #1+ match
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[-1][-1]