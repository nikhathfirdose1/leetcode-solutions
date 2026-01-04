class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxval = float("-inf")

        i = 0
        j = 1

        while j < len(prices):

            diff = prices[j] - prices[i]

            if  diff > 0:
                if diff > maxval:
                    maxval = diff
                j += 1

            else:
                i += 1
                j = i + 1

        return maxval if maxval > 0 else 0

        