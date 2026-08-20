class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.build_graph(edges)

        if self.dfs(graph,source,destination,set()):
            return True
        return False

    def dfs(self,graph,src,dst,visited):
        if src == dst:
            return True

        if src in visited:
            return False

        visited.add(src)
        for neighbor in graph[src]:
            if self.dfs(graph,neighbor,dst,visited):
                return True
        return False
    
    def build_graph(self,edges):
        graph = {}
        for edge in edges:
            src,dst = edge
            if src not in graph:
                graph[src]=[]
            if dst not in graph:
                graph[dst]=[]
            graph[src].append(dst)
            graph[dst].append(src)
        return graph