class Solution:

    def __init__(self, w: List[int]):

        self.w = w
        self.prefix = [1] * len(self.w)
        self.prefix[0] = self.w[0]

        for i in range(1,len(self.w)):
            self.prefix[i] = self.prefix[i-1] + self.w[i]
        

    def pickIndex(self) -> int:

        


        # print(self.prefix)
        total = self.prefix[-1]

        x = random.randint(1, total)

        for i in range(len(self.prefix)):
            if self.prefix[i] >= x:
                return i



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()