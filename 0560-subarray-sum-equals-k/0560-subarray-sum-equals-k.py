class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        ans = 0

        hm = {0:1}

        for num in nums:
            prefix += num
            
            if prefix - k in hm:
                ans += hm[prefix -k]
                print(f"  → Found a match! Adding {hm[prefix -k]} to ans → ans={ans}")

            hm[prefix]= hm.get(prefix, 0) + 1

        return ans
        