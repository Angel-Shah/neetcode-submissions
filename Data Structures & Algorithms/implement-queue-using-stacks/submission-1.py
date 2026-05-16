class MyQueue:

    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        if self.popStack:
            return self.popStack.pop(-1)
        else:
            for val in range(len(self.pushStack)):
                self.popStack.append(self.pushStack.pop(-1))
            return self.popStack.pop(-1)

    def peek(self) -> int:
        if self.popStack:
            return self.popStack[-1]
        return self.pushStack[0]

    def empty(self) -> bool:
        if not self.pushStack and not self.popStack:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()