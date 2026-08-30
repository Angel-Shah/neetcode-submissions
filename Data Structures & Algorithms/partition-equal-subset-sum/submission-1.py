class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums)/2

        for num in nums:
            new_dp = set()
            for t in dp:
                new_dp.add(num+t)
                new_dp.add(t)
            dp = new_dp
            if target in dp:
                return True

        return False
