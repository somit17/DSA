class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first, last = {}, {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = -1
        for ch in first:
            ans = max(ans, last[ch] - first[ch] - 1)
        return ans