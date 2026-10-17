from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_map = Counter(p)
        k = len(p)
        window = Counter(s[:k])
        start = 0
        result =[]
        if window == p_map:
            result.append(start)

        for end in range(0,len(s)-k):
            window[s[end]]-=1
            if window[s[end]] == 0:
                del window[s[end]]
            window[s[end + k]]+=1
            
            if window == p_map:
                result.append(end + 1)

        return result