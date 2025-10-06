class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0

        l = 0
        r = len(height) - 1

        l_max = height[l]
        r_max = height[r]

        while l <r:

            if height[l] <= height[r]:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]

            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]

        return res
        