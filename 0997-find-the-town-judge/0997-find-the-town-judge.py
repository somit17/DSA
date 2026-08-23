class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        indegree = [0 for i in range(0,n+1)]
        outdegree = [0 for i in range(0,n+1)]

        for edge in trust:
            node_a,node_b = edge
            outdegree[node_a]+=1
            indegree[node_b]+=1

        for person in range(1,n+1):
            if indegree[person]==n-1 and outdegree[person]==0:
                return person

        return -1