class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        ans = [1] * n
        right = 1

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        for i in range(n-1, -1, -1):
            ans[i] = right * ans[i]
            right = right * nums[i]

        return ans