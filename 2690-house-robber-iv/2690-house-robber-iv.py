class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        left = 1
        right = max(nums)

        numHouses = len(nums)

        while left < right:
            mid = (left + right) // 2

            robbed = 0

            i=0
            while i < numHouses:
                if nums[i] <= mid:
                    robbed += 1
                    i += 2
                else:
                    i += 1
                
            if robbed >= k:
                right = mid
            else:
                left = mid + 1

        return left

                




        