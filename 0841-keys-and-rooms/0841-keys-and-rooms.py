class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # graph = { i:[] for i in range(len(rooms))}
        # for i,edge in enumerate(rooms):
        #     graph[i].append(edge)
        visited = set()
        self.dfs(rooms,0,visited)
        return len(rooms) == len(visited)

    def dfs(self,rooms,node,visited):
        if node in visited:
            return 
        visited.add(node)
        for neigbor in rooms[node]:
            self.dfs(rooms,neigbor,visited)
        
        return 
        