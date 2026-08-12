class Solution:
    def isUgly(self, n: int) -> bool:
        if n > 0 and n <= 1:
            return True
        if n < 0 :
            return False
        uglyNums = set([2,3,5])
        remain = n
        while remain != 1:
            newVal = remain
            for u in uglyNums:
                if newVal%u == 0:
                    # print(f"{u} is factor of {newVal}")
                    newVal /= u
                    # print(f"newVal={newVal}")
                    break
            if newVal == remain:
                return False
            remain = newVal
        return True