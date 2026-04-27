class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = {}
        for idx,val in enumerate(nums2):
            if val not in mappings:
                mappings[val] = [idx]
            else:
                mappings[val].append(idx)
        ans = []
        for num in nums1:
            indicies = mappings[num]
            if len(indicies) == 1:
                ans.append(indicies[0])
                del mappings[num]
            else:
                ans.append(mappings[num].pop(-1))
                
        return ans
