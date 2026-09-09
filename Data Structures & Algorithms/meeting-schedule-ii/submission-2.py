"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        heap = []
        # event types -1 = start, -2=end
        for i in intervals:
            start,end = i.start,i.end
            heapq.heappush(heap,(start,-1))
            heapq.heappush(heap,(end,-2))

        max_rooms = 0
        meeting_rooms = 0
        while heap:
            time,typ = heapq.heappop(heap)
            if typ == -1:
                meeting_rooms += 1
                max_rooms = max(max_rooms,meeting_rooms)
            else:
                meeting_rooms -= 1
            

        return max_rooms