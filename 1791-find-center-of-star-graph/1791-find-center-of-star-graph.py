class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        def build_adj_list(edges):
            adj_list = {}
            for edge in edges:
                u,v = edge
                if u not in adj_list:
                    adj_list[u] = []
                if v not in adj_list:
                    adj_list[v] = []
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list
        adj = build_adj_list(edges)
        nodes = len(adj)
        for key,value in adj.items():
            if len(value) == nodes-1:
                return key
        return -1

        