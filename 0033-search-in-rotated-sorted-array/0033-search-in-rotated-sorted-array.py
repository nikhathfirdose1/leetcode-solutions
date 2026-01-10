class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = 0
        right = len(nums) - 1

        n = len(nums) - 1

        if nums[left] <= nums[right]:
            pivot = 0
        else:
            while left < right:
                mid = (left + right) // 2

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            
            pivot = left

        
        if nums[pivot] <= target <= nums[n]:
            left, right = pivot, n
        else:
            left, right = 0, pivot

        
        while left <= right:
            mid = (left+ right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1

        
        return -1

        
