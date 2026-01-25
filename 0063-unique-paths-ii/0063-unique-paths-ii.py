class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0]*cols for i in range(rows)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for i in range(1, rows):

            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0] + dp[i][0]

            

        for j in range(1, cols):

            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j-1] + dp[0][j]

        for i in range(1,rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        
        return dp[rows-1][cols-1]
        