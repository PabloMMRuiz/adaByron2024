from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        i = 0
        #como les gusta hacer implementaciones horrendas
        while i < len(manager):
            if manager[i] != -1:
                graph[manager[i]].append(i)
            i+=1
        maxTime = 0
        queue = deque()
        queue.append((headID, 0))
        print(graph)
        while queue:
            currNode, time = queue.popleft()
            print(currNode)
            #si hacemos bfs en un arbol, no hay que mirar ningun visited dado que solo se llega por un camino a cada vertice
            if time > maxTime:
                maxTime = time
            for e in graph[currNode]:
                queue.append((e, time+informTime[currNode]))
        return maxTime