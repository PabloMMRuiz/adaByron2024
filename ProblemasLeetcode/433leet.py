from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        #Para acceso mas rapido al banco de genes
        queue = deque()
        queue.append((startGene, 0))
        visited = set()
        visited.add(startGene)
        chars = "ACGT"
        while queue:
            currGene, dis = queue.popleft()
            i = 0
            while i <8:
                for c in chars:
                    newGene :str= currGene[:i]+c+currGene[i+1:]
                    if newGene in visited:
                        continue
                    if newGene not in bank:
                        continue
                    if newGene == endGene:
                        return dis+1
                    else:
                        queue.append((newGene, dis+1))
                        visited.add(newGene)
                i+=1
        return -1