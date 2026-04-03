class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        l,r = -1,0
        while r < len(nums):
            if nums[r] == val:
                r += 1
                count += 1
                continue
            l+= 1
            # print(f"l:{l},r:{r}")
            nums[l] = nums[r]
            r+= 1

        return len(nums) - count