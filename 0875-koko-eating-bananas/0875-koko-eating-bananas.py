class Solution:
    def minEatingSpeed(self, apples: List[int], h: int) -> int:


        def total(rate):
            time = 0

            for i in range(len(apples)):
                time += (apples[i] + rate - 1) // rate
            
            return time

        
        left = 1
        right = max(apples)

        while left < right:
            mid = (left+right)// 2

            if total(mid) > h:
                left = mid + 1
            else:
                right = mid
        
        return left
