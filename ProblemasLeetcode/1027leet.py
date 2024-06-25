class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Dictionary to store the length of the arithmetic subsequence
        # dp[i][d] will store the length of the longest arithmetic subsequence ending at index i with difference d
        dp = {}
        max_length = 0

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if (j, diff) in dp:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                else:
                    dp[(i, diff)] = 2  # At least two elements (nums[j] and nums[i])
                
                max_length = max(max_length, dp[(i, diff)])
        
        return max_length
