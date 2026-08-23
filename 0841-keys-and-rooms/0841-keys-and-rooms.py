class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms,0,visited)
        n = len(rooms)
        return n == len(visited)


    def dfs(self,rooms,node,visited):
        if node in visited:
            return 
        visited.add(node)
        for neighbor in rooms[node]:
            self.dfs(rooms,neighbor,visited)