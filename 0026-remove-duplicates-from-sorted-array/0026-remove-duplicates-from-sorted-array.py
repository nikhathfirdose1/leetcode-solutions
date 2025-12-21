class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        i = 0

        for key, val in hm.items():

            nums[i] = key

            i += 1

        return len(hm)



    





        
