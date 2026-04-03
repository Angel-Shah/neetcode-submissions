class Solution:
    def twoSum(self, arr, target) -> List[List[int]]:
        l,r = 0,len(arr)-1
        ans = []
        while l<r:
            currSum = arr[l]+arr[r]
            if currSum == target:
                ans.append([arr[l],arr[r]])
                l +=1 
                r = len(arr)-1
            if currSum < target:
                l +=1
            if currSum > target:
                r -= 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        foundTargets = {}
        nums = sorted(nums)
        for idx,num in enumerate(nums):
            currTarget = num
            if currTarget not in foundTargets:
                currArr = nums[:idx]+nums[idx+1:]
                res = self.twoSum(currArr, currTarget*-1)
                # print(f"target:{currTarget}, arr:{currArr} , twoSum found:{res}, num:{num}")
                if res:
                    for r in res:
                        r.append(num)
                        r = sorted(r)
                        found = False
                        for li in result:
                            if li == r:
                                found = True
                                # print("already in result")
                        if not found:
                            # print("newResult adding now")
                            result.append(r)
                foundTargets[currTarget]=0
        return result