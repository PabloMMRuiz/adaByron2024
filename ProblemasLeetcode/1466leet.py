from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        queue = deque()
        queue.append(0)
        visited = set()
        visitedEdges = set()
        tree = {v:[-1,-1] for v in range(n)}
        while queue:
            currNode = queue.popleft()
            
        return res