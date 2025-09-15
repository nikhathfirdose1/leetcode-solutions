class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first():
            l = 0
            r = len(nums) - 1

            res = -1

            while l <= r:
                mid = (l +r) // 2

                if nums[mid] == target:
                    res = mid
                    r = mid - 1

                elif target < nums[mid]:
                    r = mid - 1

                else:
                    l = mid + 1

            return res


        def second():
            l = 0
            r = len(nums) - 1

            res = -1

            while l <= r:
                mid = (l +r) // 2

                if nums[mid] == target:
                    res = mid
                    l = mid + 1

                elif target < nums[mid]:
                    r = mid - 1

                else:
                    l = mid + 1

            return res


        return [first(), second()]

