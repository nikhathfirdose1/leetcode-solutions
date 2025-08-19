class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hm = {0:1}

        prefix = 0

        ans = 0

        for num in nums:
            prefix += num

            if prefix - k in hm:
                ans += hm[prefix-k]

            hm[prefix] = hm.get(prefix, 0) + 1

        return ans

        