class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_q = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while mono_q and nums[mono_q[-1]] < nums[r]:
                mono_q.pop()
            mono_q.append(r)
            
            if l > mono_q[0]:
                mono_q.popleft()
            
            if (r+1) >= k:
                res.append(nums[mono_q[0]])
                l += 1
            
        return res
         

'''
Input: nums = [1,2,1,0,4,2,6], k = 3

max_arr = [1,2,2,2,4,4,6]

opp_arr = []

Output: [2,2,4,4,6]

'''