from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for n in nums:
            if n in freq_dict:
                freq_dict[n] += 1
            else:
                freq_dict[n] = 1
        sorted_freq_dict = list(sorted(freq_dict.items(),key=lambda x:x[1],reverse=True))
        ans = []
        for i in range(k):
            ans.append(sorted_freq_dict[i][0])
        return ans