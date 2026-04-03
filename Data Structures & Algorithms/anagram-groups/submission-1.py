from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        similar_idx_arr ={}
        for i,s in enumerate(strs):
            curr_counter = hash(frozenset(Counter(s).items()))
            if curr_counter in similar_idx_arr:
                similar_idx_arr[curr_counter].append(s)
            else:
                similar_idx_arr[curr_counter] = [s]
        ans_arr = []
        for key,val in similar_idx_arr.items():
            ans_arr.append(val)

        return ans_arr
        