class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        max_len = 0
        count = 0

        hm = {0:-1}

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1        
            else:
                count += 1

            if count in hm:
                max_len = max(max_len, i - hm[count])
            else:
                hm[count] = i

        return max_len
        