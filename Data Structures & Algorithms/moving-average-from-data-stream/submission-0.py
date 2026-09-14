class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.queue = deque()
        self.running_sum = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.running_sum += val
        if len(self.queue) > self.window:
            self.running_sum -= self.queue.popleft()
        return self.running_sum/len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
