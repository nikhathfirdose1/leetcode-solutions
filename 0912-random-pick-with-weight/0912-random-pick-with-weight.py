class Solution:

    def __init__(self, w: List[int]):

        self.prefix_sum_list = []
        prefix_sum = 0

        for w1 in w:
            prefix_sum += w1
            self.prefix_sum_list.append(prefix_sum)

        self.total = prefix_sum
        

    def pickIndex(self) -> int:

        target = self.total * random.random()

        for i, pre in enumerate(self.prefix_sum_list):
            if target < pre:
                return i

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()