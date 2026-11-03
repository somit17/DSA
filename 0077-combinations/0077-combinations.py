class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []
        def dfs(num):
            if len(path) == k:
                result.append(path[:])
                return
            
            if num > n:
                return

            #Include
            path.append(num)
            dfs(num+1)
            #Exclude
            path.pop()
            dfs(num+1)
        dfs(1)
        return result
        