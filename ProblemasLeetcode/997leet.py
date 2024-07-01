from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        edges = defaultdict(list)
        for p1, p2 in trust:
            edges[p1].append(p2)
        for p in range(1,n+1):
            if p not in edges.keys():
                #This means p does not trust anyone
                isTrustedByEveryone = True
                for p2 in range(1,n+1):
                    if p == p2: 
                        continue
                    if isTrustedByEveryone == False:
                        break
                    else:
                        if p2 not in edges:
                            isTrustedByEveryone = False
                            break
                        if p not in edges[p2]:
                            isTrustedByEveryone = False
                            break
                if isTrustedByEveryone:
                    return p
        return -1