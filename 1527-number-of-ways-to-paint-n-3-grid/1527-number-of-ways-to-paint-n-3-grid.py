class Solution:
    def numOfWays(self, n: int) -> int:

        mod = 10**9 + 7
        
        type1 = 6  
        type2 = 6 

        for _ in range(2, n + 1):
            new_type1 = (3 * type1 + 2 * type2) % mod
            new_type2 = (2 * type1 + 2 * type2) % mod
            type1, type2 = new_type1, new_type2

        return (type1 + type2) % mod
