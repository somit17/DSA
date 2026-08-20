class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj_list = {}
        for edge in edges:
            src,dst = edge
            if src not in adj_list:
                adj_list[src]=[]
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        n = len(adj_list) - 1
        for node in adj_list:
            if len(adj_list[node]) == n:
                return node
        return -1

        