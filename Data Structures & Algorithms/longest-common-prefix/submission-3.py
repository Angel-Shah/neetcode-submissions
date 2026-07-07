class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 1
        for x in range(len(strs[0])):
            for s in strs:
                if strs[0][:i] not in s:
                    return strs[0][:i-1]
            i += 1
        return strs[0]
        