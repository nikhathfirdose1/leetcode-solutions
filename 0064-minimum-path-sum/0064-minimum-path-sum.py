class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]


        print(dp)


        for row in range(1, rows):
            for col in range(1, cols):

                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]


        return dp[rows-1][cols-1]
