class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = [1] * len(self.w)
        self.prefix[0] = self.w[0]

        for i in range(1, len(self.w)):
            self.prefix[i] = self.prefix[i-1] + self.w[i]       

    def pickIndex(self) -> int:

        left = 0
        right = len(self.prefix) - 1

        last = self.prefix[-1]

        target = random.randint(1, last)

        while left < right:

            mid = (left+right) // 2

            if self.prefix[mid] < target:
                left = mid + 1
            else:
                right = mid

        
        return left
  


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()