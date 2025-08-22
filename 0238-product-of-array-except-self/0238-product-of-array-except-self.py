class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        zero_count = 0
        prod = 1
        ans = [0] * (len(nums))

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num
        

        if zero_count > 1:
            return ans

        if zero_count == 1:

            idx = nums.index(0)
            ans[idx] = prod
            return ans

        for i in range(len(nums)):
            res = prod // nums[i]
            ans[i] = res

        return ans


        
