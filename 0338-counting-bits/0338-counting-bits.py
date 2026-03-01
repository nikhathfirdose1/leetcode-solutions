class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]
        
        
        res = [0] * (n + 1)

        res[0] = 0

        for i in range(1, n+1):
            if i % 2 == 0:
                res[i] = res[i // 2] 
            else:
                res[i] = res[i // 2] + 1

        return res