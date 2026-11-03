class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def dfs(open,close,s):
            if open == n and close == n:
                result.append(s)
                return

            if open < n:
                dfs(open + 1,close,s + '(')
                
            if close < open:
                dfs(open, close + 1,s + ')')

        dfs(0,0,'')
        return result