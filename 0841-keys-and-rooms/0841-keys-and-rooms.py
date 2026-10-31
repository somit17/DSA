class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # graph = {i:[] for i in range(len(rooms))}
        # for i,edges in enumerate(rooms):
        #     graph[i].append(edges)
        visited = set()
        self.dfs(rooms,0,visited)
        return len(visited) == len(rooms)

    def dfs(self,rooms,node,visited):
        if node in visited:
            return 
        
        visited.add(node)

        for neighbor in rooms[node]:
            self.dfs(rooms,neighbor,visited)
        
        return 