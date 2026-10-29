class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        num_parents = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        
        for edge in prerequisites:
            u,v = edge
            graph[v].append(u)
            num_parents[u]+=1
        order = []    
        ready = [k for k,v in num_parents.items() if v == 0]
        if len(ready) == 0:
            return False
        while ready:
            node = ready.pop()
            order.append(node)
            for child in graph[node]:
                num_parents[child]-=1
                if num_parents[child] == 0:
                    ready.append(child)
        
        return len(order) == numCourses

        
        