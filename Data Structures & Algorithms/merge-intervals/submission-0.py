class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])

        ans = [intervals[0]]
        for curr_start,curr_end in intervals[1:]:
            if curr_start <= ans[-1][1]:
                ans[-1][1] = max(curr_end,ans[-1][1])
            else:
                ans.append([curr_start,curr_end])
        return ans