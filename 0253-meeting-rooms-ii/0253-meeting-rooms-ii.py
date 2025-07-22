class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        heap = []
        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)


            heapq.heappush(heap, interval[1])


        return len(heap)
        