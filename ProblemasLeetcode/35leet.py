class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            k = (i + j) // 2
            if nums[k] == target:
                return k
            elif nums[k] < target:
                i = k + 1
            else:
                j = k - 1
        return i


