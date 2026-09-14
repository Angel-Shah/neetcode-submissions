class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for idx,val in enumerate(intervals):
            curr_start,curr_end = val[0],val[1]

            if newInterval[1] < curr_start: #case 1
                res.append(newInterval)
                return res + intervals[idx:]
            elif newInterval[0] > curr_end: #case 2
                res.append(val)
            else:
                new_start = min(curr_start,newInterval[0])
                new_end = max(curr_end,newInterval[1])
                newInterval = [new_start,new_end]

        res.append(newInterval)
        return res


'''
case 1: (completely before)
|--A--| |--B--| => |---New--| |--A--| |--B--|

case 2: (completely after)
|--A--| |--B--| => |--A--| |--B--||---New--|
                    

case 2: (overlapping interval)
|--A--| |--B--| => |--A--| |--B--|
                      |---New--|


'''