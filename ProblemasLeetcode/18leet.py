class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)==4 and sum(nums)==target:
            return [nums]
        nums.sort()
        res = []

        for i in range(len(nums)-3):
            #skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                k = j+1
                l = len(nums)-1
                while k<l:
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total == target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        # Skip duplicate elements for the third number
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        # Skip duplicate elements for the fourth number
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k+=1
                        l-=1
                    elif total<target:
                        k+=1
                    else:
                        l-=1
        return res
