class Solution:

    def __init__(self, w: List[int]):

        self.w = w

        self.prefix = [0] * len(self.w)
        self.prefix[0] = self.w[0]

        for i in range(1, len(self.w)):
            self.prefix[i] = self.prefix[i-1] + self.w[i]

        

    def pickIndex(self) -> int:

        last = self.prefix[-1]
        target = random.randint(1, last)

        l = 0
        r = len(self.prefix) - 1

        while l < r:
            m = (l+r) // 2

            if self.prefix[m] < target:
                l = m + 1
            else:
                r = m

        return l      


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()