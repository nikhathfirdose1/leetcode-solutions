class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix = 0
        ans = 0

        hm = {0:1}

        for num in nums:
            prefix += num

            if prefix - goal in hm:
                ans += hm[prefix - goal]

            hm[prefix] = hm.get(prefix, 0) + 1

        return ans
        