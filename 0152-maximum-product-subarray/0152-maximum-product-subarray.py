class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_max = nums[0]
        curr_min = nums[0]
        max_prod = curr_max
        

        for i in range(1,len(nums)):

            prev_max, prev_min = curr_max, curr_min
            curr_max = max(nums[i],prev_max* nums[i], prev_min*nums[i])
            curr_min = min(nums[i],prev_max* nums[i], prev_min*nums[i])


            max_prod = max(max_prod, curr_max)

        return max_prod
