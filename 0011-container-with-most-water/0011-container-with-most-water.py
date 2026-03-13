class Solution:
    def maxArea(self, height: List[int]) -> int:


        # Assumptions:
        # 1. Wont have negative inputs as the height of line needs to always be positive
        # 2. height array is never empty 
        

        # Clarifying:
        # 1. COuld you give me avergae input size ? okay if its 10^5 a linear solution is needed becuase if we have a n^n solution then it will lead to a slow output
        # 2. can i modify the given inpout?
        # 3. how high can the indidivusal height[i] be?


        # Edge Cases:
        # 1. all values equal -> len(height) * any value
        
        
        max_so_far = 0

        i = 0
        j = len(height) - 1

        while i < j:

            area = min(height[i], height[j]) * (j-i)
            max_so_far = max(max_so_far, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        
        return max_so_far


# Dry Run

# height = [ 7,5,4,8,3,2,1]
# output = 21

# i = 0; j = 6; area = 6
# i = 0; j = 5; area = 10
# i = 0; j = 4; area = 12
# i = 0; j = 3; area = 21
# i = 1; j = 3; area = 10
# i = 2; j = 3; area = 4
# i = 3; j = 3




