class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        memo = {}

        

        def helper(n):

            if n == 0:
                memo[n] = 0

            if n == 1:
                return nums[0]
            
            if n in memo:
                return memo[n]

            
            memo[n] = max(helper(n-1), (helper(n-2)+nums[n-1]))


            return memo[n]


        
        return helper(len(nums))
        
