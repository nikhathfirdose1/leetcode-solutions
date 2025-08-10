class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = float('inf')
        ans = 0

        for price in prices:

            if price < min_val:
                min_val = price

            else:

                ans = max(ans, price - min_val)

        return ans




        