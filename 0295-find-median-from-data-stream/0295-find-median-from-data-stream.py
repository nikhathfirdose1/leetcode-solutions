class MedianFinder:

    def __init__(self):

        self.high = [] #min-heap of big numbers
        self.low = [] #max-heap of small numbers
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)

        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

        
        

    def findMedian(self) -> float:

        if len(self.low) > len(self.high):
            return -self.low[0]

        else:
            return (-self.low[0] + self.high[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()