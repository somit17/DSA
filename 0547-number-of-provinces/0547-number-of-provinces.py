class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        total_nodes = len(isConnected)
        graph = {i:[] for i in range(total_nodes)} 
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and j!=i:
                    graph[i].append(j)
        #print(graph)
        visited = set()
        count = 0
        for i in range(total_nodes):
            if i not in visited:
                self.dfs(graph,i,visited)
                count+=1
        return count

    def dfs(self,graph,src_node,visited):
        if src_node in visited:
            return 

        visited.add(src_node)

        for n in graph[src_node]:
            if n not in visited:
                self.dfs(graph,n,visited)

        return 
        