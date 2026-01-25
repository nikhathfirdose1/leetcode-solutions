class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        self.w = []

        for x1, y1, x2, y2 in self.rects:
            w = (x2-x1 + 1) * (y2-y1 +1)
            self.w.append(w)

        self.prefix = [0] * len(self.w)
        self.prefix[0] = self.w[0]

        for i in range(1, len(self.w)):
            self.prefix[i] = self.prefix[i-1] + self.w[i]

        self.last = self.prefix[-1]


    def pick(self) -> List[int]:

        left=0
        right = len(self.prefix) - 1

        target = random.randint(1, self.last)

        while left < right:
            mid = (left+right) // 2

            if self.prefix[mid] < target:
                left = mid + 1

            else:
                right = mid

        ax1, ay1, ax2, ay2 = self.rects[left]

        x = random.randint(ax1, ax2)
        y = random.randint(ay1, ay2)

        return [x,y]


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()