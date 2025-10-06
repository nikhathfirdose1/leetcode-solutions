class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i-1]:
                continue
 
            left = i + 1
            right = len(nums) - 1

            while left < right:

                sum_val = num + nums[left] + nums[right]

                if sum_val > 0:
                    right -=1 

                elif sum_val < 0:
                    left += 1

                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left -1]:
                        left += 1


        return ans

        