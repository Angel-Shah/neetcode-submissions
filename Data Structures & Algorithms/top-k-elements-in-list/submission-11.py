from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for n in nums:
            if n in freq_dict:
                freq_dict[n] += 1
            else:
                freq_dict[n] = 1
        freq = [[] for i in range(len(nums)+1)]

        for key,val in freq_dict.items():
            freq[val].append(key)
        
        ans = []
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
    
