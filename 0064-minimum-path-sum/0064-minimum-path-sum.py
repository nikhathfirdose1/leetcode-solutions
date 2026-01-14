class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        # if rows == 1 or cols == 1:
        #     return grid[0][0]

        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = grid[0][0]

        for col in range(1, cols):
            dp[0][col] = dp[0][col-1] + grid[0][col]

        for row in range(1, rows):
            dp[row][0] = dp[row-1][0] + grid[row][0]

        print(dp)
        for i in range(1,rows):
            for j in range(1,cols):

                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        

        return dp[rows-1][cols-1]

        