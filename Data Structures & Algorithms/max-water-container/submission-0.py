class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        water = 0
        while l< r:
            currArea = min(heights[l],heights[r])*(r-l)
            water = max(water,currArea)
            if heights[l] > heights[r]:
                r -= 1;
            else:
                l +=1
        return water