class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max = 0
        while i<=j:
            vol = (j-i)*min(height[i],height[j])
            if vol > max:
                max = vol
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max
