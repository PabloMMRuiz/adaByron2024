class Solution:
    def bipartito(self,graph,i,color,diccionario):
        if i in diccionario:
            if color != diccionario[i]:
                return False
            else:
                return True
        
        diccionario[i]=color
        siguiente = 0
        if color==0:
            siguiente = 1
        for vecino in graph[i]:
            if not self.bipartito(graph,vecino,siguiente,diccionario):
                return False
        
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n_vertices = len(graph)
        color_vertice = {}

        while len(color_vertice)<n_vertices:
            for i in range(n_vertices):
                if i not in color_vertice:
                    random = i
                    break
            
            if not self.bipartito(graph,random,0,color_vertice):
                return False
        
        return True

