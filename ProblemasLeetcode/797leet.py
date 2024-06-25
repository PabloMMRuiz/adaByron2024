class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        currPath = []
        def dfs(node: int, currPath: list, res: list):
            newCurrPath = currPath.copy()
            newCurrPath.append(node)
            if node == len(graph)-1:
                res.append(newCurrPath)
            else:
                for n in graph[node]:
                    dfs(n, newCurrPath, res)
        dfs(0, currPath, res)
        return res
