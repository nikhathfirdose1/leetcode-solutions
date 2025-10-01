class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = {}

        bucket= [[] for i in range(len(nums) + 1)]

        ans = []

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        
        for key, freq in hm.items():
            bucket[freq].append(key)

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans            

        
