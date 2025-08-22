class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        right = 1

        ans = [1] *n

        for i in range(n-1):
            prod = ans[i] * nums[i]
            ans[i+1] = prod


        for i in range(n-1,-1,-1):
            ans[i] *= right
            right = nums[i] * right


        return ans

        