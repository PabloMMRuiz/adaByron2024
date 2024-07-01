from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        res = 0
        # Buscamos isla:
        visited = set()
        i, j = 0, 0
        def isleFinder(i_0 , j_0):
            firstRow = True
            for i in range(i_0, len(grid)):
                if firstRow:
                    for j in range(j_0, len(grid[0])):
                        if grid[i][j]=="1" and (i, j) not in visited:
                            return (i, j)
                    firstRow = False
                else:
                    for j in range(0, len(grid[0])):
                        if grid[i][j]=="1" and (i, j) not in visited:
                            return (i, j)
            return 0
        def isleRegister(startpos):
            moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            
            visited.add(startpos)
            queue = deque()
            queue.append(startpos)
            while queue:
                currI, currJ = queue.popleft()
                # Posibles movimientos: vamos solo por tierra
                for cI, cJ in moves:
                    newI = currI+cI
                    newJ = currJ+cJ
                    if 0> newI or newI >= len(grid) or 0>newJ or newJ >= len(grid[0]):
                        continue
                    if (newI, newJ) in visited:
                        continue
                    elif grid[newI][newJ] == "1":
                        visited.add((newI, newJ))
                        queue.append((newI, newJ))
        while True:
            tmp = isleFinder(i, j)
            if tmp == 0:
                return res
            else:
                res+=1
                i, j = tmp[0], tmp[1]
                isleRegister((i, j))