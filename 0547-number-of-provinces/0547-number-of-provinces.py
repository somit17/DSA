class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edges = []
        for row in range(n):
            for col in range(row + 1,n):
                if isConnected[row][col] == 1:
                    edges.append((row,col))
        #print(graph)
        roots = [i for i in range(n)]
        sizes = [1 for i in range(n)]

        for edge in edges:
            node_a,node_b = edge
            self.union(roots,sizes,node_a,node_b)


        count = 0
        for i in range(0, n):
            if roots[i] == i:
                count += 1
        return count

    def union(self,roots,sizes,node_a,node_b):
        root_a = self.find(roots,node_a)
        root_b = self.find(roots,node_b)
        if root_a == root_b:
            return 

        if sizes[root_a] > sizes[root_b]:
            roots[root_b] = root_a
            sizes[root_a] += sizes[root_b]
        else:
            roots[root_a] = root_b
            sizes[root_b] += sizes[root_a]

    def find(self,roots,node):
        if roots[node] == node:
            return node
        found = self.find(roots,roots[node])
        return found

