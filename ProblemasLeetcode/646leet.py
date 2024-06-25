class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Step 1: Sort the pairs based on the second element of each pair
        pairs.sort(key=lambda x: x[1])
        
        # Step 2: Initialize the DP array
        n = len(pairs)
        dp = [1] * n  # Each pair can at least form a chain of length 1 by itself

        # Step 3: Fill the DP array
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:  # If pair j can chain to pair i
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Step 4: Compute the result
        return max(dp)