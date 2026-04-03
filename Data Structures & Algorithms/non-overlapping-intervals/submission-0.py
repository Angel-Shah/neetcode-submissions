class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        ans = 0
        for start, end in intervals[1:]:
            if start >= prevEnd: # no overlap
                prevEnd = end
            else: # there is overlap
                prevEnd = min(prevEnd, end)
                ans += 1
        return ans