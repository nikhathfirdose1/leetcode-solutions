class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = {}
        heap = []

        ans= []

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        
        for key, v in hm.items():

            heapq.heappush(heap, (v,key))

            if len(heap) > k:
                heapq.heappop(heap)

        for val, key in heap:
            ans.append(key)       

        return ans
