class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')  
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == target:
                    return target  
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum > target:
                    k -= 1
                else:
                    j += 1
        
        return closest_sum