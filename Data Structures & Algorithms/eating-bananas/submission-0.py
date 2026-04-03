class Solution:
    def numHourstoEat(self, piles,k):
        ans = 0
        for p in piles:
            ans += (p//k)
            if p%k != 0:
                ans += 1
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)

        ans = h

        while low <= high:
            # print(f"low:{low}, high:{high}")
            mid = (low+high)//2
            # print(f"mid:{mid}")
            currHours = self.numHourstoEat(piles,mid)
            # print(f"currHours:{currHours}")
            if currHours > h :
                low = mid + 1
            else:
                # low = mid + 1
                ans = mid
                high = mid - 1
                continue
        return ans