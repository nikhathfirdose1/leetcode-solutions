class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1


        rem = k
        for i in range(len(count)-1, -1,-1):
            rem -= count[i]

            if rem <= 0:
                return i + min_value

        return -1