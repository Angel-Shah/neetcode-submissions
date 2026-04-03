
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = [0]*26
        windowCounts = [0]*26
        # print(ord('a')) // 97

        #builds the s1 frequency count array
        for c in s1:
            s1Counts[ord(c)-97] += 1

        print(f"s1 count: {s1Counts}")
        
        #now we iterate over s2 with fixed sliding window of size len(s1)
        l,r = 0,0
        while r < len(s2):
            windowCounts[ord(s2[r])-97] += 1
            #you aren't at the fixed size yet, increase r pointer
            if r-l+1 < len(s1):
                r += 1
                continue
            
            #at this point it means we have reached len(s1) window
            if s1Counts == windowCounts:
                return True
    
            windowCounts[ord(s2[l])-97] -= 1
            l+=1
            r+=1     

        return False

                