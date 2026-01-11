class Solution:
    def missingNumber(self, nums):

        first = sum(nums)
        second = 0

        for i in range(len(nums) + 1):
            second += i

        return second - first