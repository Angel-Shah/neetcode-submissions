class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        # print(ord('A')) 65
        l,r = 0,0
        longest = 0
        maxFreq = 0
        while r < len(s):
            freq[ord(s[r])-65] += 1
            maxFreq = max(maxFreq,freq[ord(s[r])-65])
            # print(f"freq:{freq}, maxFreq:{maxFreq}")

            if r-l +1 -maxFreq > k:
                # print("hit limit, moving left pointer")
                freq[ord(s[l])-65] -= 1
                l += 1
            else:
                # print("found a new longest")
                longest = max(longest, r-l+1)

            r += 1

        return longest

