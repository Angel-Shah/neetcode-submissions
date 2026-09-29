class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for curr_start,curr_end in intervals[1:]:
            #current start is overlap with prev end
            if curr_start <= result[-1][1]:
                result[-1][1] = max(result[-1][1],curr_end)
            else:
                #no overlap, we can insert new interval
                result.append([curr_start,curr_end])
        return result