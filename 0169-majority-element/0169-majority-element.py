class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        major = n // 2

        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        for key, value in hm.items():
            if value > major:
                return key

                

        