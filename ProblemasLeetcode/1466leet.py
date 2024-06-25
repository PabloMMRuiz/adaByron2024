from collections import deque, defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        queue = deque()
        queue.append(0)
        edges = defaultdict(list)
        #pasamos las aristas a un formato mas eficiente
        for c in connections:
            edges[c[0]].append(c)
            edges[c[1]].append(c)
        visited = set()
        visitedEdges = set()
        while queue:
            currNode = queue.popleft()
            if currNode in visited:
                continue
            else:
                visited.add(currNode)
                #hacemos esto por que "creamos" ciclos al coger aristas del reves. La implementacion de m* es lo que tiene
                for start, end in edges[currNode]:
                    if (start, end) in visitedEdges:
                        continue
                    if end == currNode:
                        queue.append(start)
                        visitedEdges.add((start, end))
                    elif start == currNode:
                        visitedEdges.add((start, end))
                        queue.append(end)
                        res+=1
        return res