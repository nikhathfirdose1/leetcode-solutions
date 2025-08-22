class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        

        s = len(sequence)
        w = len(word)

        dp = [0] * (s+1)

        ans = 0


        for i in range(w,s+1):

            
            if sequence[i-w:i] == word:
                dp[i] = dp[i-w] + 1
                ans = max(ans, dp[i])


            # print(dp)

        return ans
