class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        roots = [i for i in range(0,n+1)]
        sizes = [1 for i in range(0,n+1)]

        for edge in edges:
            node_a,node_b = edge
            if not self.union(roots,sizes,node_a,node_b):
                return edge
        return []
        
    def union(self,roots,sizes,node_a,node_b):
        root_a = self.find(roots,node_a)
        root_b = self.find(roots,node_b)

        if root_a == root_b:
            return False

        if sizes[root_a] > sizes[root_b]:
            roots[root_b] = roots[root_a]
            sizes[root_a]+=sizes[root_b]
        else:
            roots[root_a] = roots[root_b]
            sizes[root_b]+=sizes[root_a]
        return True


    def find(self,roots,node):
        if roots[node] == node:
            return node

        found = self.find(roots,roots[node])
        return found