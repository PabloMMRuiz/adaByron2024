class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        i = 0
        bestDiff = False
        while i + k <= len(nums):
            print( nums[i+k-1] - nums[i])
            if not bestDiff or nums[i+k-1] - nums[i] < bestDiff:
                bestDiff = nums[i+k-1] - nums[i]
                
            i +=1
        if not bestDiff:
            return 0
        return bestDiff