from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        anagram_map = Counter(p)
        k = len(p)
        start = 0 
        result = []
        s_map = Counter(s[:k])
        if s_map == anagram_map:
            result.append(start)
        
        for end in range(0,len(s)-k):
            trailing_char = s[end]
            leading_char = s[end + k]
            s_map[trailing_char]-=1
            s_map[leading_char]+=1
            if anagram_map == s_map:
                result.append(end+1)

        return result

        