class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevEnd = float('-inf')
        interva = 0
        for start, end in intervals:
            if start >= prevEnd: # no overlap
                prevEnd = end
                interva += 1
        return len(intervals) - interva