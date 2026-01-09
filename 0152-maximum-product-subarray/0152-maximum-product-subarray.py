class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cand = []
        best = float("-inf")

        prev_max = 1
        prev_min = 1

        for num in nums:
            cand.append(num)
            cand.append(num * prev_max)
            cand.append(num * prev_min)

            new_max = max(cand)
            new_min = min(cand)

            best = max(new_max, best)

            prev_max, prev_min = new_max, new_min
            cand =[]

        return best
        