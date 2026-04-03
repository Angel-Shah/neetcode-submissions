class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevEnd = float('-inf')
        picked = 0
        for start, end in intervals:
            if start >= prevEnd: # no overlap
                prevEnd = end
                picked += 1
        return len(intervals) - picked