class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        
        def val(c: str) -> int:
            if c <= 'b': 
                return 1
            idx = ord(c) - ord('c')  
            return 2 + idx // 3      

        n = len(word)
        arr = [val(ch) for ch in word]

        
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + arr[i]

        ans = 0
        for l in range(n):
            for r in range(l, n):
                total = P[r+1] - P[l]
                length = r - l + 1
                if total % length == 0:
                    ans += 1
        return ans
