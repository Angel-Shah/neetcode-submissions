class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
      
        if len(self.stack) != 0:
            self.minVal = min(self.minVal,val)
        else:
            self.minVal = val
        self.stack.append((val,self.minVal))
        print(f"current stack: {self.stack}")
        print(f"current minVal: {self.minVal}")

    def pop(self) -> None:
        self.stack.pop(-1)
        if self.stack:
            self.minVal = self.stack[-1][1]



    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return int(self.stack[-1][1])