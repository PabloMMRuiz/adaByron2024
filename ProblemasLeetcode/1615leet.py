from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)

        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)

        return max(
            len(graph[i]) + len(graph[j]) - (i in graph[j])
            for i in range(n)
            for j in range(i + 1, n)
        )
#Esto tiene que poder hacerse ligeramente mas eficiente en la practica, pero teoricamente esto es lo q hay