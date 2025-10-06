class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        max_val = 0

        while l < r:

            w = r -l
            h = min(height[l], height[r])

            area = w * h
            max_val = max(max_val, area)

            if height[l] > height[r]:
                r -= 1

            else:
                l += 1

        return max_val


        