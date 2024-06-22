class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second last row and move upwards
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # For each element, choose the minimum path sum of the two adjacent elements in the row below
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        # The top element now contains the minimum path sum
        return triangle[0][0]
                
