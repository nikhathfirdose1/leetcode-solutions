class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        ans = 0
        max_val = 0

        hm = {0:-1}

        for i, num in enumerate(nums):
            prefix += num 

            if prefix - k in hm:
                ans = max(ans, i- hm[prefix - k])

            if prefix not in hm:
                hm[prefix] = i


        return ans


        