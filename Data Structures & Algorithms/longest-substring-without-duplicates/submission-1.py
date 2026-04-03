class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l,r = 0,0
        longest = 0
        while r< len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                longest = max(longest,r-l+1)
                r += 1
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
        return longest



