"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# time-complexity: O(nlogn)
# space-complexity: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sweep = defaultdict(int)

        for i in intervals:
            sweep[i.start] += 1
            sweep[i.end] -= 1
        
        ans = 0
        curr = 0
        for key in sorted(sweep.keys()):
            curr += sweep[key]
            ans = max(ans,curr)

        return ans
