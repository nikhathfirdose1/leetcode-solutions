class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # Clarifying Questions:
        # 1. input is expeted to have negatives 0s and positive values right?
        # 2. will i atleast have min 3 values in my input?
        # 3. what is the expected length of this array nums? 
        # 5. can i modify the input??

        # Edge Cases:
        # 1. expected to return if all values are 0? return any 3 index?
        # 2. multiple pairs with 0 but all are same values on different index? -> no duplicate triplets
        # 3. No pair sums up to 0? - return []


        # nums = [-1,0,1,3,-2,-1]
        # output = [(-1,0,1), (3,-2,-1)]


        nums.sort()
        
        result = set()

        for i in range(len(nums)):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen = set()

            for j in range(i+1, len(nums)):

                compliment = - (nums[i] + nums[j])


                if compliment in seen:

                    triplet = tuple(sorted((nums[i], nums[j], compliment)))

                    result.add(triplet)


                seen.add(nums[j])

        
        return [list(triplet) for triplet in result]
