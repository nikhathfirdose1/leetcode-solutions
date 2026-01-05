class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        maxV= nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0

            currSum += num

            maxV = max(maxV, currSum)

        return maxV