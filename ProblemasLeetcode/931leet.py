class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #caso base n=1 y n=2
        if len(matrix)==1:
            return matrix[0][0]
        if len(matrix)==2:
            return min(matrix[0][0]+matrix[1][0],matrix[0][0]+matrix[1][1],matrix[0][1]+matrix[1][0],matrix[0][1]+matrix[1][1])
        #en cada capa el minimo 
        for i in range(1,len(matrix)):
            for j in range(len(matrix)):
                if j == 0:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1])
                elif j == len(matrix)-1:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j-1])
                else:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1])
        #devuelvo el minimo de la ult capa
        return min(matrix[-1])