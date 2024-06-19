from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        answer = [0]+[-1 for _ in range(n-1)]
        visited = set()
        queue = deque()
        queue.append((0, 'red', 0))
        queue.append((0, 'blue', 0))
        #vaya horror las aristas maaan
        #pues bfs puro, con doble camino basicamente
        while queue:
            currNode, color, dist = queue.popleft()
            if (currNode, color) in visited:
                continue
            else:
                visited.add((currNode, color)) 
                answer[currNode]=dist if answer[currNode]==-1 else answer[currNode] #el por que de esto: puede que tengamos que visitar
                #un nodo mas de una vez, para poder salir de el con otro color. Pero solo queremos pillar la distancia la primera vez que lo visitemos
                #la eficiencia se podria mejorar implementando dos visited por que esto no es muy eficiente, pero paso
                #y, sobre todo, no usando esa basura de implementacion de grafos
                neighboursOtherColor = []
                for edge in redEdges if color == "blue" else blueEdges:
                    if edge[0]==currNode:
                        neighboursOtherColor.append(edge[1])
                for neighbour in neighboursOtherColor:
                    queue.append((neighbour, "red" if color == "blue" else "blue", dist+1))
        return answer
