class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left = [1] * n
        right = [1] * n

        ans = [1] *n

        for i in range(n-1):
            prod = left[i] * nums[i]
            left[i+1] = prod

        for i in range(n-1,0,-1):
            # print(i)
            prod = right[i] * nums[i]
            right[i-1] = prod

        for i in range(n):
            ans[i] = left[i] * right[i]

        return ans

        