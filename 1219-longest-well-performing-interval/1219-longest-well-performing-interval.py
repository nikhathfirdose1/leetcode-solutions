class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        prefix = 0
        first = {}
        ans = 0



        for i, hr in enumerate(hours):

            prefix += 1 if hr > 8 else -1

            if prefix >0:
                ans = i + 1
            
            else:
                if prefix - 1 in first:
                    ans = max(ans, i - first[prefix-1])

            if prefix not in first:
                first[prefix] = i

        
        return ans

