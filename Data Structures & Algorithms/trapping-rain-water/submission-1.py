class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        water = 0
        l,r = 0, len(height)-1
        max_l = height[l]
        max_r = height[r]

        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l,height[l])
                water += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r,height[r])
                water += max_r - height[r]
        return water