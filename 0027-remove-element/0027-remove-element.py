class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        read = 0
        write = 0

        for i in range(len(nums)):

            if nums[read] != val:
                nums[write] = nums[read]
                read += 1
                write += 1

            else:
                read += 1
                


        return write
