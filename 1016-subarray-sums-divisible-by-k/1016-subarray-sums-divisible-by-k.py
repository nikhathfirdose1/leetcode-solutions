class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix = 0
        ans = 0
        hm = {0:1}

        for i, num in enumerate(nums):
            prefix += num


            if prefix % k in hm:
                ans += hm[prefix % k] 


            hm[prefix%k] = hm.get(prefix %k, 0) + 1

        print(hm)

        return ans
        