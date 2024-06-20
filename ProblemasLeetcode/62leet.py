class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #mariz en la q va cuantos caminos hay para cada i, j
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                #los caminos para llegar a i,j son los de arriba más los de la izquierda
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
        
