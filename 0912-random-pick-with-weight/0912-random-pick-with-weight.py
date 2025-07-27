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

        l, h = 0 , len(self.prefix_sum_list) - 1

        while l < h:
            mid = (l+h) // 2

            if target > self.prefix_sum_list[mid]:
                l = mid + 1
            else:
                h = mid

        return l




        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()