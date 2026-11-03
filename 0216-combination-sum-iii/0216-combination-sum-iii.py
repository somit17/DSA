class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        path = []

        def dfs(num,total):
            if total > n or len(path) > k:
                return 

            if total == n:
                if len(path) == k:
                    result.append(path[:])
                    return
            if num > 9:
                return 
            #Include next element
            path.append(num)
            dfs(num + 1,total + num)
            #Remove element
            path.pop()
            dfs(num + 1,total)



        dfs(1,0)
        return result