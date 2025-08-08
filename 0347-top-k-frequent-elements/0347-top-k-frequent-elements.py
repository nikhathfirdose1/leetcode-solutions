class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        ans = []
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        for key, val in hm.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
            
        for pair in heap:
            ans.append(pair[1])

        return ans




        