from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or len(s1) > len(s2):
            return False

        #per_map
        s1_map = Counter(s1)
        k = len(s1)
        s_map = Counter(s2[:k])
        if s1_map == s_map:
            return True

        for end in range(len(s2)-k):
            trailing_char = s2[end]
            leading_char = s2[end+k]
            s_map[trailing_char]-=1
            if s_map[trailing_char] == 0:
                del s_map[trailing_char]
            s_map[leading_char]+=1
            if s1_map == s_map:
                return True 

        return False