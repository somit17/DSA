class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        ans = set()
        for x in words:
            for y in words:
                if x!=y and x in y:
                    ans.add(x)

        print(ans)
        return list(ans)