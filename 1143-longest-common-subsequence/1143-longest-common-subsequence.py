class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i,j,memo):
            #Base case
            if i == len(text1) or j == len(text2):
                return 0
            state = (i,j)
            if state in memo:
                return memo[state]
            if text1[i]==text2[j]:
                return 1 + dfs(i + 1,j + 1,memo)
            else:
                skip_text1 = dfs(i + 1,j,memo)
                skip_text2 = dfs(i,j + 1,memo)
                memo[state]= max(skip_text1,skip_text2)
            return memo[state]
        return dfs(0,0,{})

