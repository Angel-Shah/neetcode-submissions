class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = {}
        for idx,val in enumerate(nums2):
            if val not in mappings:
                mappings[val] = set([idx])
            else:
                mappings[val].add(idx)
        ans = []
        for num in nums1:
            ans.append(mappings[num].pop())

        return ans
