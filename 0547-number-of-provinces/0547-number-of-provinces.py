class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = {i: [] for i in range(n)}
        visited = [False] * n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)

        def dfs_explore(node):
            if visited[node]:
                return 
            visited[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_explore(neighbor)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs_explore(i)
                count+=1
        return count