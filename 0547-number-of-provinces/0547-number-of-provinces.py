class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        # adj = {i: [] for i in range(n)}
        
        # for i in range(n):
        #     for j in range(n):
        #         if isConnected[i][j] == 1 and i != j:
        #             adj[i].append(j)

        def dfs_explore(node):
            if visited[node]:
                return 
            visited[node] = True
            
            for neighbor in range(n):
                if not visited[neighbor] and isConnected[node][neighbor] == 1:
                    dfs_explore(neighbor)

        def bfs_explore(start_node):
            queue = deque([start_node])
            visited[start_node] = True
            
            while queue:
                current_node = queue.popleft()  # BFS: popleft, not pop
                
                # Check ALL neighbors (0 to n-1)
                for neighbor in range(n):  
                    if not visited[neighbor] and isConnected[current_node][neighbor] == 1:
                        visited[neighbor] = True
                        queue.append(neighbor)

        count = 0
        for i in range(n):
            if not visited[i]:
                bfs_explore(i)
                count+=1
        return count