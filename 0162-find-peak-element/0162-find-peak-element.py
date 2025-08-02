class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))


        return heap[0][1]




        