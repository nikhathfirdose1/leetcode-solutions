class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)

        dp =[[0]* (i+1) for i in range(rows)]
        dp[0][0] = triangle[0][0]

        for r in range(1, rows):
            for c in range(r+1):

                if c == 0:
                    dp[r][c] = dp[r-1][c] + triangle[r][c]

                elif c == r:
                    dp[r][c] = dp[r-1][c-1] + triangle[r][c]

                else:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c]) + triangle[r][c]

        
        return min(dp[rows-1])
        