class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #Como funciona esto: supongamos que el grafo no tiene aristas de corte: entonces podemos construir un ciclo que lo recorra

        #Si hacemos dfs desde el 0, dando la vuelta al ciclo vamos a llegar de nuevo al 0. 
        #Rank: cuando aparece el nodo i en el dfs
        #Lowest rank: el nodo con el rank mas bajo al que esta conectado (que no es su padre en el dfs)

        #Por que esto descubre las aristas de corte: Si no hay un ciclo por culpa de una arista, el vertice hijo de esa relacion no va a volver a poder conectarse al
        #resto del dfs ya hecho: su lowest rank va a ser el mismo. Luego si el rank del padre es mayor que el lowest rank de su hijo, ahi hay un problema en el ciclo
        rank = [None] * n
        lowest_rank = [None] * n
        
        # CREATE THE GRAPH
        g = [[] for _ in range(n)]
        for c in connections:
            g[c[0]].append(c[1])
            g[c[1]].append(c[0])       
        
        # DFS FROM NODE 0
        critical = []
        self.dfs(g, 0, None, set(), rank, lowest_rank, critical)
        return critical
        
        
    def dfs(self, g, curr, parent, vis, rank, lowest_rank, critical):
        
        # BASE CASE - NODE HAS BEEN VISITED
        if curr in vis:
            return
        
        # ADD TO VISITED
        vis.add(curr)
        
        # SET THE NODE'S RANK AND LOWEST RANK BY DEFAULT
        rank[curr] = len(vis)
        lowest_rank[curr] = len(vis)
        
        # EXPLORE ITS NEIGHBOURS
        for nb in g[curr]:
            
            # DO NOT EXPLORE THE NODE YOU CAME FROM
            if nb == parent:
                continue
              
            # EXPLORE MY NEIGHBOURS
            self.dfs(g, nb, curr, vis, rank, lowest_rank, critical)
            
            # UPDATE MY LOWEST RANK
            lowest_rank[curr] = min(lowest_rank[curr], lowest_rank[nb])
            
            # CHECK IF CRITICAL
            if lowest_rank[nb] > rank[curr]:
                critical.append([curr, nb])

