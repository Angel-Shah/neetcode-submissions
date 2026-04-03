class Solution:
    def isHappy(self, n: int) -> bool:
        found = {}
        currNum = n
        while True:
            sumSquared = 0
            temp = abs(currNum) # Work with the absolute value
            while temp > 0:
                rem = temp % 10 # Extract the last digit
                sumSquared += rem * rem # Square the digit and add to total
                temp //= 10 # Remove the last digit
            if sumSquared == 1:
                return True
            if sumSquared in found:
                return False
            else:
                found[sumSquared] = True
                currNum = sumSquared
            
            