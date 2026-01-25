class Solution:
    def uniquePaths(self, m: int, n: int) -> int:



        dp = [[0]*n for i in range(m)]

        dp[0][0] = 1

        

        for row in range(1,m):
            dp[row][0] = dp[row-1][0] + dp[row][0]


        for col in range(1,n):
            dp[0][col] = dp[0][col-1] + dp[0][col]  

           


        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        


        return dp[m-1][n-1] 