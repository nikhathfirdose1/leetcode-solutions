class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0 
        j = len(height) - 1
        best = 0

        while i < j:
            chosen_height = min(height[i], height[j])
            width = j - i

            area =  chosen_height * width

            best = max(best, area)

            if height[i] <= height[j]:
                i += 1
            
            else:
                j -= 1

        return best


        