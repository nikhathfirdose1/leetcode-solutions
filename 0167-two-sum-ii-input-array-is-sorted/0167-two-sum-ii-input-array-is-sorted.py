class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            sum_val = numbers[right] + numbers[left]

            if  sum_val == target:

                return [left+1, right+1]

            elif sum_val < target:

                left += 1

            else:
                right -= 1


        return [-1,-1]

