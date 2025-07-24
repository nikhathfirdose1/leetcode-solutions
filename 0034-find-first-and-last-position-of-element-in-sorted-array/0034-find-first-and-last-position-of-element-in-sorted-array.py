class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def left():
            left = 0
            right = len(nums) - 1

            while left+ 1 < right:

                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid

                else:
                    right = mid

            if nums[left] == target:
                return left

            if nums[right] == target:
                return right

            return -1
            

        def right():
            left = 0
            right = len(nums) - 1

            while left+ 1 < right:

                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid

                else:
                    left = mid

            if nums[right] == target:
                return right

            if nums[left] == target:
                return left

            

            return -1


        if not nums:
            return [-1, -1]
        
        l = left()
        r = right()

        if l != -1:
            return [l,r]
        else:
            return [-1,-1]