class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        maxSum = nums[0]
        prefix = 0

        for i in range(len(nums)):

            if prefix < 0:
                prefix = 0

            prefix += nums[i]
            
            maxSum = max(maxSum, prefix)

        
        return maxSum