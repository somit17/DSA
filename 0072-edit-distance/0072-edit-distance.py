class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        m, n = len(word1), len(word2)

        def dfs(i, j):
            if i == m:
                return n - j          # insert remaining chars of word2
            if j == n:
                return m - i          # delete remaining chars of word1

            state = (i, j)
            if state in memo:
                return memo[state]

            if word1[i] == word2[j]:
                memo[state] = dfs(i + 1, j + 1)      # match, no cost
            else:
                memo[state] = 1 + min(
                    dfs(i + 1, j),       # delete word1[i]
                    dfs(i, j + 1),       # insert word2[j]
                    dfs(i + 1, j + 1)    # replace
                )
            return memo[state]

        return dfs(0, 0)