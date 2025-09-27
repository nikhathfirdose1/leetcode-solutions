class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:

        def val(c):

            if c <= "b":
                return 1
            else:
                return 2 + (ord(c) - ord("c")) // 3


        ans = 0

        for i in range(1,10):
            prefix = 0
            freq = {0:1}

            for ch in word:
                prefix += val(ch) - i
                ans += freq.get(prefix, 0)

                freq[prefix] = freq.get(prefix,0) + 1

        return ans
        









