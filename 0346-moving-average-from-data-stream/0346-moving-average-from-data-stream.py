class MovingAverage:

    def __init__(self, size: int):

        self.queue = deque()
        self.size = size
        

    def next(self, val: int) -> float:

        self.queue.append(val)

        if len(self.queue) > self.size:
            self.queue.popleft()

        if self.queue:
            total = sum(self.queue) 
            res = total / len(self.queue)
            return res


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)