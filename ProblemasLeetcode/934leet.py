from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Buscamos isla:
        isla = False
        i, j = 0, 0
        found = False
        for fila in grid:
            for col in fila:
                if col == 1:
                    startpos = (i, j)
                    found = True
                    break
                j += 1
            if found:
                break
            i += 1
            j = 0
        # Ahora partimos desde la isla. Vamos a registrar la isla completa
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
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
                elif grid[newI][newJ] == 1:
                    visited.add((newI, newJ))
                    queue.append((newI, newJ))
        #Una vez hemos registrado la primera isla, partimos desde ella a distancia 0, buscamos la segunda isla: el primer 1 que nos encontremos
        queue =deque()
        for isla1 in visited:
            queue.append((isla1, 0))
        #bfs solucion
        while queue:
            currPos, dis = queue.popleft()
            currI, currJ = currPos
            # Posibles movimientos: vamos solo por tierra
            for cI, cJ in moves:
                newI = currI+cI
                newJ = currJ+cJ
                if 0> newI or newI >= len(grid) or 0>newJ or newJ >= len(grid[0]):
                    continue
                if (newI, newJ) in visited:
                    continue
                elif grid[newI][newJ] == 1:
                    return dis
                else:
                    visited.add((newI, newJ))
                    queue.append(((newI, newJ), dis+1))
