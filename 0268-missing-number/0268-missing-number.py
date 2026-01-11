class Solution:
    def missingNumber(self, nums):

        expected = 0
        for i in range(len(nums)+1):
            expected = expected ^ i

        actual = 0
        for num in nums:
            actual = actual ^ num

        print(expected,actual)

        return actual ^ expected