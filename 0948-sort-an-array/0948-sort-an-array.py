class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        ans = []
        heapq.heapify(nums)

        while nums:
            small = heapq.heappop(nums)
            ans.append(small)

        return ans




            
        