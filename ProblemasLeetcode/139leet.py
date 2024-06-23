class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a set from wordDict for faster lookups
        word_set = set(wordDict)
        # Initialize dp array where dp[i] means s[0:i] can be segmented
        dp = [False] * (len(s) + 1)
        # Base case: an empty string can be segmented
        dp[0] = True
        
        # Iterate over all positions in the string
        for i in range(1, len(s) + 1):
            # Check each substring s[j:i]
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
    
    # Return whether the entire string can be segmented
        return dp[len(s)]      




            