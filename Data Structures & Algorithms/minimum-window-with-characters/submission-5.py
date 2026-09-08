class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        s_counts = {}
        t_counts = {}
        

        for c in t:
            t_counts[c] = 1 + t_counts.get(c,0)

        found,need = 0,len(t_counts)
        ans = [-1,-1]
        ans_len = float('inf')
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            s_counts[c] = 1 + s_counts.get(c,0)
            if c in t_counts and s_counts[c] == t_counts[c]:
                    found += 1
                    
            while found == need:
                if (r-l+1) < ans_len:
                    ans_len = r-l+1
                    ans = [l,r]
                
                s_counts[s[l]] -= 1
                if s[l] in t_counts and s_counts[s[l]] < t_counts[s[l]]:
                    found -= 1
                l += 1
            
        if ans_len == float('inf'):
            return ""
        else:
            return s[ans[0]:ans[1]+1]
        