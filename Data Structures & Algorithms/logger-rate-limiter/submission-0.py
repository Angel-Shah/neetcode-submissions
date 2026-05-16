class Logger:

    def __init__(self):
        self.nextAllowed = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.nextAllowed:
            self.nextAllowed[message] = timestamp + 10
            return True
        if timestamp >= self.nextAllowed[message]:
            self.nextAllowed[message] = timestamp + 10
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
