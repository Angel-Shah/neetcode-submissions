"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        prev_end = float('-inf')
        for i in intervals:
            start,end = i.start,i.end
            if start < prev_end:
                return False
            prev_end = end
        return True