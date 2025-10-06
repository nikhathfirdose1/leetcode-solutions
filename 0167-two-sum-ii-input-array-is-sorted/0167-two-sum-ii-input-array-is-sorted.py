class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hm = {}

        for i, num in enumerate(numbers):

            if target - num in hm:
                return [hm[target - num] + 1, i+1]

            hm[num] = i  
