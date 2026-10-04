class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        graph = self.buildGraph(paths)
        # return self.dfs(graph,)

        for node in graph:
            if len(graph[node]) == 0:
                return node

    
    def buildGraph(self,paths):
        graph = {}
        for path in paths:
            src,dst = path[0],path[1]
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)
        print(graph)
        return graph
    # def dfs(self,graph,src):
    #     for neighbor in graph[src]:

        #pass

        