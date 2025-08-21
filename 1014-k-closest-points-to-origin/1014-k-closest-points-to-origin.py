class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        ans = []

        for point in points:

            val = (point[0] * point[0]) + (point[1]*point[1])

            heapq.heappush(heap, (-val, point))

            
            if len(heap) > k:
                heapq.heappop(heap)
            
        for pair in heap:
            ans.append(pair[1])

        return ans