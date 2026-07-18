class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for edge in prerequisites:
            u = edge[0]
            v = edge[1]
            #v->u
            graph[v].append(u)
            indegree[u]+=1

        def topologicalSort(graph,indegree):
            queue = deque()
            count = 0
            for i in range(numCourses):
                if indegree[i] == 0:
                    queue.append(i)
                    count += 1
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    indegree[neighbor]-=1
                    if indegree[neighbor]==0:
                        queue.append(neighbor)
                        count+=1
            if count == numCourses: #Was able to finisihc couses
                return True
            return False



        
        return topologicalSort(graph,indegree)
        