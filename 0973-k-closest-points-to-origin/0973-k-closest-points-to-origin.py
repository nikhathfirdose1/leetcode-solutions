import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        ans = []

        for x, y in points:          
            dist = sqrt(x*x+ y*y)

            heapq.heappush(heap, (-dist, x,y))

            if len(heap) > k:
                heapq.heappop(heap)

        for dist, x, y in heap:
            ans.append([x,y])

        return ans

