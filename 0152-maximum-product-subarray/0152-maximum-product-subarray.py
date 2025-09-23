class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_max = nums[0]
        curr_min = nums[0]
        max_prod = curr_max
        

        for i in range(1,len(nums)):
            temp = max(nums[i], max(curr_max* nums[i], curr_min*nums[i]))
            curr_min = min(nums[i], min(curr_max* nums[i], curr_min*nums[i]))

            curr_max = temp

            max_prod = max(max_prod, curr_max)

        return max_prod
