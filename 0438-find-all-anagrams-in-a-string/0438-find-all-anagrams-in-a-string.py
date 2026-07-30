class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        window = []
        counter_p = Counter(p)
        p_len = len(p)
        for i in range(len(s)):
            window.append(s[i])
            if len(window) > p_len:
                window.pop(0)
            if len(window) == p_len and Counter(window)==counter_p:
                result.append(i - p_len + 1)
        print(result)
        return result
        