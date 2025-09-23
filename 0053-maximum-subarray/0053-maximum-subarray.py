class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        max_sum = float("-inf")

        for idx in range(len(nums)):
            curr_sum = max(0, curr_sum) + nums[idx]

            max_sum = max(max_sum, curr_sum)

        return max_sum
        