class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return self.rec(maze, entrance, 0, [])

    
    def rec(self, maze: List[List[str]], entrance: List[int], step: int, visited: List[Tuple[int]]) -> int:
        x = entrance[0]
        y = entrance[1]
        
        if step>0 and (x-1<0 or y-1<0 or x+1>=len(maze) or y+1>=len(maze[0])):
            return step
        
        else:
            moves = []
            if x-1>=0 and maze[x-1][y] == '.' and (x-1,y) not in visited: #l
                moves.append('l')
            if y-1>=0 and maze[x][y-1] == '.' and (x,y-1) not in visited: #d
                moves.append('d')
            if x+1<len(maze) and maze[x+1][y] == '.' and (x+1,y) not in visited: #r
                moves.append('r')
            if y+1<len(maze[0]) and maze[x][y+1] == '.' and (x,y+1) not in visited: #u
                moves.append('u')
            
            if not moves:
                return -1

            else:
                step = step+1
                visited.append((x, y))
                l = -1
                d = -1
                r = -1
                u = -1
                for m in moves:
                    if m == 'l':
                        l = self.rec(maze, [x-1, y], step, visited)
                    if m == 'd':
                        d = self.rec(maze, [x, y-1], step, visited)
                    if m == 'r':
                        r = self.rec(maze, [x+1, y], step, visited)
                    if m == 'u':
                        u = self.rec(maze, [x, y+1], step, visited)
                res = -1
                for s in [l, d, r, u]:
                    if s>0:
                        if (res>0 and s<res) or res<0:
                            res = s
                return res


# Solucion pablo
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