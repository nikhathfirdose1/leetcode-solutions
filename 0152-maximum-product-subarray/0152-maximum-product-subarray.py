class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        best = prev_max = prev_min = nums[0]

        for i in range(1, len(nums)):
            a = nums[i]
            b = nums[i] * prev_max
            c = nums[i] * prev_min

            new_max = max(a,b,c)
            new_min = min(a,b,c)

            best = max(new_max, best)

            prev_max, prev_min = new_max, new_min

        return best
        