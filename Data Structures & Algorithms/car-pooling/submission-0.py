class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sweep = defaultdict(int)
        for num_passengers,start,end in trips:
            sweep[start] += num_passengers
            sweep[end] -= num_passengers
        
        curr_count = 0
        for time in sorted(sweep.keys()):
            curr_count += sweep[time]
            if curr_count > capacity:
                return False
        return True
