class Solution:
    def numDecodings(self, s: str) -> int:
        
        # if 1 -> next can be :{0,1,2,3,4,5,6,7,8,9}
        # if 2 -> next can be :{0,1,2,3,4,5,6}
        cache = {len(s):1}

        def dfs(idx):
            if idx in cache:
                return cache[idx]
            if s[idx] == '0':
                return 0
            
            #take one
            ans = dfs(idx+1)
            
            #take both
            if idx+1 < len(s):
                if s[idx] == "1" or (s[idx] == "2" and s[idx+1] in "0123456"):
                    ans += dfs(idx+2)

            cache[idx] = ans
            return ans

        return dfs(0)