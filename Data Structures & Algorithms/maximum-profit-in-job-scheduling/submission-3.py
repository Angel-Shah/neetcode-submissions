import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # dp problem with memoization

        # at each event, we either decide to include it and then look for the next start time of an event that is greater than the current event you picked's end time.

        # if you decide not to include the current event, thne you can simply go on to the next event

        # inorder to make this work we will need to sort by start-time
        events = []
        for i in range(len(startTime)):
            events.append([startTime[i],endTime[i],profit[i]])

        events.sort()

        cache = {}
        def dfs(i,curr_profit):
            if i == len(startTime):
                return curr_profit
            if (i,curr_profit) in cache:
                return cache[(i,curr_profit)]
            
            #try taking this event
            next_idx = bisect.bisect_left(events,events[i][1],key=lambda x:x[0])
            take = dfs(next_idx, curr_profit + events[i][2])

            #don't take
            dont = dfs(i+1,curr_profit)

            ans = max(take,dont)
            cache[(i,curr_profit)] = ans
            return ans

        return dfs(0,0)
            
