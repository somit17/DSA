class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dest = len(graph)-1
        print(f'D - > {dest}')
        return self.dfs(graph,0,dest)

    def dfs(self,graph,node,dest):

        if node == dest:
            return [[node]]
        paths = []
        for neighbor in graph[node]:
            neighbor_paths = self.dfs(graph,neighbor,dest)
            for neighbor_path in neighbor_paths:
                #neighbor_path.append(node)
                paths.append([node] + neighbor_path)
        return paths


    
        