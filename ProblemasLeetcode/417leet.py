class Solution:
    def pacificAtlantic(self, heights):
        #A cell can flow into both if:
        #It is one of the corners (up-right or bottom-left)
        #It can reach one of those corners
        visited = set()
        pacific = set()
        atlantic = set()
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfsA(pos):
            atlantic.add(pos)
            i, j = pos[0], pos[1]
            posH = heights[i][j]
            for cI, cJ in moves:
                newI = i+cI
                newJ = j+cJ
                if 0> newI or newI >= len(heights) or 0>newJ or newJ >= len(heights[0]):
                    continue
                elif heights[newI][newJ]<posH:
                    continue
                elif (newI, newJ) in atlantic:
                    continue
                else:
                    dfsA((newI, newJ))                
        def dfsP(pos):
            pacific.add(pos)
            i, j = pos[0], pos[1]
            posH = heights[i][j]
            for cI, cJ in moves:
                newI = i+cI
                newJ = j+cJ
                if 0> newI or newI >= len(heights) or 0>newJ or newJ >= len(heights[0]):
                    continue
                elif heights[newI][newJ]<posH:
                    continue
                elif (newI, newJ) in pacific:
                    continue
                else:
                    dfsP((newI, newJ))  
        #Check which squares run into the atlantic:
        for i in range(len(heights)):
            dfsA((i, len(heights[0])-1))
        for j in range(len(heights[0])):
            dfsA((len(heights)-1, j))
        #Check which ones run into the pacific
        for i in range(len(heights)):
            dfsP((i, 0))
        for j in range(len(heights[0])):
            dfsP((0, j))
        return list(atlantic.intersection(pacific))
