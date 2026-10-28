class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = {i:[] for i in range(n)}
        for edge in edges:
            u,v = edge
            graph[u].append(v)
            graph[v].append(u)

        return self.dfs(graph,source,destination,{})

    def dfs(self,graph,src,dst,visited):
        if src == dst:
            return True
        if src in visited:
            return False
        visited[src] = True
        for child in graph[src]:
            if self.dfs(graph,child,dst,visited):
                return True

        return False
        