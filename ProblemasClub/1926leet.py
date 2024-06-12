from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        queue.append(entrance)
        moves = 0
        visited = set()
        while queue:
            moves +=1
            #posibles movimientos
            # [1,0], [-1, 0], [0, 1], [0, -1]
            pos = queue.popleft()
            posMoves = []
            for move in [[1,0], [-1, 0], [0, 1], [0, -1]]:
                newPos = [pos[0]+move[0], pos[1]+move[1]]
                if newPos in visited:
                    continue
                #comprobamos que sea un vertice legal:
                if newPos[0] <0 or newPos[0] >= len(maze) or newPos[1] < 0 or newPos[1] >= len(maze[0]):
                    continue
                if maze[newPos[0]][newPos[1]] == "+":
                    continue
                if newPos[0] ==0 or newPos[0] == len(maze) or newPos[1] == 0 or newPos[1] == len(maze[0]):
                    return moves
                queue.append(newPos)
        return -1