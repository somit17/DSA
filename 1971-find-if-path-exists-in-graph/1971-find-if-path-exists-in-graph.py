class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def build_adj_list(edges):
            adj = {}
            for edge in edges:
                u,v = edge
                if u not in adj:
                    adj[u]=[]
                if v not in adj:
                    adj[v]=[]
                adj[u].append(v)
                adj[v].append(u)
            return adj
        #adjacency list
        adj = build_adj_list(edges)

        def dfs(adj,src,dst,visited):
            if src == dst:
                return True
            if src in visited:
                return False
            visited.add(src)
            for neighbor in adj[src]:
                if dfs(adj,neighbor,dst,visited):
                    return True
            
            return False
        
        def bfs():
            queue = deque([source])
            visited = {source}
            while queue:
                node = queue.popleft()
                if node == destination:
                    return True
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return False
        return bfs()
        