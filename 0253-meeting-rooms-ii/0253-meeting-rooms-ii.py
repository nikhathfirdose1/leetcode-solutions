class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda interval: interval[0])
            
        heap = []
        room = 0
        for interval in intervals:
            heapq.heappush(heap, interval[1])

        
        for interval in intervals:
            start = interval[0]

            if start >= heap[0]:
                heapq.heappop(heap)
            else:
                room += 1

        return room


        

