class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        num_parents = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            num_parents[u]+=1
            graph[v].append(u)
        #print(graph)
        ready = [node for node in num_parents if num_parents[node] == 0]
        #print(ready)
        order = []
        while ready:
            node = ready.pop()
            order.append(node)    
            for child in graph[node]:
                num_parents[child]-=1
                if num_parents[child] == 0:
                    ready.append(child)

        return order if len(order) == numCourses else []


        