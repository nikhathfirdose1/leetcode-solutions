class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        

        p2 = 0
        p1 = nums[0]

        for i in range(2, n+1):
            curr = max(p1, (p2 + nums[i-1]))
            p2 = p1
            p1 = curr

        return p1
        