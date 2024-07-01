from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for source, target in edges:
            graph[target].append(source) #Y por que esto al reves?:
        #A todo target se tiene que poder llegar desde algun lado
        #Cual es ese lado en concreto nos da igual debido a que no hay ciclos:
        #Si partimos desde todo vertice que no sea target vamos a acabar llegando a ese vertice
        #Y ademas todos esos vertices van a tener que estar si o si en la solucion
        #Asi que vamos a contar los vertices a los que no llega nadie: en vez de poner un vertice y sus vecinos (outgoing edges)
        #Ponemos un vertice y los que llegan a el (incoming)
        #Los que esten vacios, son la solucion
        res = []
        for v in range(n):
            if len(graph[v])==0:
                res.append(v)
        return res