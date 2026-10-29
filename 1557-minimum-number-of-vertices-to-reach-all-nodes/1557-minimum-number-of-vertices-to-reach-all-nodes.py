class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        num_parents = {i:0 for i in range(n)}
        for edge in edges:
            u,v = edge
            num_parents[v]+=1
        
        return [ k for k,v in num_parents.items() if v == 0 ]
        