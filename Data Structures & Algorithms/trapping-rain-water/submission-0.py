class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l,r = 0,len(height)-1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if maxL > maxR:
                r -=1
                waterToAdd = min(maxL,maxR)- height[r]
                if waterToAdd > 0:
                    water += waterToAdd
                maxR = max(maxR,height[r])
            else:
                l += 1
                waterToAdd = min(maxL,maxR)- height[l]
                if waterToAdd > 0:
                    water += waterToAdd
                maxL = max(maxL,height[l])
                
        return water