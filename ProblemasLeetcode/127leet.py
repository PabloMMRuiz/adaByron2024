from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        visited.add(beginWord)
        queue = deque()
        queue.append((beginWord, 1)) #este 1 es rarete, cosas del planteamiento del problema
        if endWord not in wordList:
            return 0
        def difIn1(s1:str, s2:str)->bool:
            difs = 0
            for e1, e2 in zip(s1, s2):
                if e1 != e2:
                    difs +=1
                if difs > 1:
                    return False
            return True if difs == 1 else False

        while queue:
            currWord, dis = queue.popleft()
            #Esto es ridiculamente ineficiente pero vamos a probar
            for word in wordList:
                if word in visited:
                    continue
                if difIn1(word, currWord):
                    if word == endWord:
                        return dis+1
                    queue.append((word, dis+1))
                    visited.add(word)
        return 0
