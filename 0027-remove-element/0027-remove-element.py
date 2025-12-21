class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nums.sort()


        for i in range(len(nums) - 1, -1, -1):
            # print(nums[i])
            if nums[i] == val:
                nums.remove(nums[i])

        return len(nums)
        