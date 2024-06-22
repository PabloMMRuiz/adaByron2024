class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        # Create the grid for dynamic programming
        dp = [[0] * m for _ in range(n)]

        # Initialize the starting point
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1

        # Initialize the first row
        for j in range(1, m):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]

        # Initialize the first column
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

        # Fill in the rest of the dp array
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]