class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        output = [0]*len(temperatures)
        for idx,temp in enumerate(temperatures):
            if not tempStack or temp < tempStack[-1][0]:
                tempStack.append((temp,idx))
            else:
                while tempStack and temp > tempStack[-1][0]:
                    popVal= tempStack.pop()
                    output[popVal[1]] = idx - popVal[1]
                # if tempStack:
                #     output[tempStack[-1][1]] = idx - tempStack[-1][1]
                tempStack.append((temp,idx))
        return output
