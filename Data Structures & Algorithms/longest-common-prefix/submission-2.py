class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = ""
        i = 1
        for x in range(len(strs[0])):
            # prefix += strs[0][i]
            # print(f"on iteration:{x}, curr prefix:{prefix}")
            for s in strs:
                if strs[0][:i] not in s:
                    # print(f"couldn't find prefix {prefix}, in {s}, returning {prefix[:-1]}")
                    return strs[0][:i-1]
            i += 1
        return strs[0]
        