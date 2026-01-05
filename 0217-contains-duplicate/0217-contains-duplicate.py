class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        
        for key, val in hm.items():
            if val > 1:
                return True

        
        return False
        