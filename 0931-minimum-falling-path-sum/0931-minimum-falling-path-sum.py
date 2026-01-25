class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]* cols for i in range(rows)]

        for i in range(cols):
            dp[0][i] = matrix[0][i]


        for i in range(1, rows):
            for j in range(cols):

                best = dp[i-1][j]

                if j-1>= 0:
                    best = min(best, dp[i-1][j-1]) 

                if j + 1< cols:
                    best = min(best, dp[i-1][j+1]) 
            
                dp[i][j] = matrix[i][j] + best

        
        return min(dp[rows-1])




        
        