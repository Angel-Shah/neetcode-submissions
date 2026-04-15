'''
[-2,0,3,-5,2,-1]

sum = -3

leftSum = [-2,-2,1,-4,-2,-3]



0+1=1

[0,2]=> 0 + 1 =1
[2,5] => -2 +
[0,5]


'''


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.prefixSum[i+1] = self.prefixSum[i]+nums[i]


    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1]-self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)