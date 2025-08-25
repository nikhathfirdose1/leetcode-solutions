class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        ans = [1] * n
        right = 1

        for i in range(1,n):
            ans[i]= ans[i-1] * nums[i-1]

        for i in range(n-1, -1, -1):
            ans[i] = right * ans[i]
            right = right * nums[i]

        # suffix[n-1] = 1

        # for i in range(n):
        #     ans[i] = prefix[i] * suffix[i]

        return ans



        