class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Initialize the dp table
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the table
        for l in range(2, n + 1):  # l is the length of the substring
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    if l == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The result is in dp[0][n-1]
        return dp[0][n-1]
