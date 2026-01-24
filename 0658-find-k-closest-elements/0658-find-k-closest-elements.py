import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap = []
        ans = []

        for num in arr:
            heapq.heappush(heap, (-abs(x-num), -num))

            if len(heap) > k:
                heapq.heappop(heap)

        for diff, num in heap:
            ans.append(-num)

        return sorted(ans)

        