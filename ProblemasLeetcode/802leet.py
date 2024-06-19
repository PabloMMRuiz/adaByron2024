class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node]=True

            for nei in graph[node]:
                if dfs(nei):
                    return True
            #Si llegamos por un ciclo, nunca ejecutaremos la siguiente linea, con lo cual se devolvera true
            #Si llegamos por dos caminos distintos, el primero lo va a dejar en false, y se devolvera false
            visited[node]=False

        for i in range(len(graph)):
            if not dfs(i):
                res.append(i)

        return res