'''
hashmap ={

"key" : [[timestamp,value]]

}


'''

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        #if key not in store return ""
        if key not in self.store:
            return ""
        # perform binary-search to find the first index where the time > timestamp
        l,r = 0,len(self.store[key])-1
        ans = ""
        while l <= r:
            mid = (l+r)//2
            curr_time,curr_val = self.store[key][mid]
            if curr_time <= timestamp:
                ans = curr_val
                l = mid + 1
            else:
                r = mid - 1
 
        return ans
        
