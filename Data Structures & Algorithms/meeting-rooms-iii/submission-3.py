class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings_taken = [0]*n
        rooms = [(0,i) for i in range(n)]
        heapq.heapify(rooms)
        # while rooms:
        #     print(heapq.heappop(rooms))
        meetings.sort(key=lambda x: x[0])
        for start,end in meetings:
            # print(f"looking at meeting :[{start},{end}]")
            while rooms and rooms[0][0] < start:
                curr_free_end,curr_free_room = heapq.heappop(rooms)
                heapq.heappush(rooms,(start,curr_free_room))
            curr_free_end,curr_free_room = heapq.heappop(rooms)
            meetings_taken[curr_free_room] += 1
            new_start = max(curr_free_end,start)
            new_end = new_start + (end-start)
            heapq.heappush(rooms,(new_end,curr_free_room))

        sorted_rooms = [(idx,val) for idx,val in sorted(enumerate(meetings_taken), key= lambda x: (x[1],-x[0]))]
        
        return sorted_rooms[-1][0]
