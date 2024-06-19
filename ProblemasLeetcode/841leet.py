
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #Que si solo hay una componente conexa, y si llegamos a ella desde el 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbour in rooms[node]:
                if neighbour in visited:
                    continue
                else:
                    dfs(neighbour)
        dfs(0)
        if list(visited) != list(range(len(rooms))):
            return False
        return True