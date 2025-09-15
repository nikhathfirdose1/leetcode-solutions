class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:

            if nums[left] <= nums[right]:
                return nums[left]

            mid = (left + right) // 2

            prev = (mid + n - 1) % n
            nxt = (mid + 1) % n

            if nums[prev] >= nums[mid] and nums[nxt] >= nums[mid]:
                return nums[mid]

            elif nums[left] <= nums[mid]:
                left = mid + 1

            elif nums[mid] <= nums[right]:
                right = mid - 1

        return -1
        