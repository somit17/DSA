class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        k = len(s1)
        window_counter = Counter(s2[:k])
        if window_counter == s1_counter:
            return True
        for end in range(len(s2) - k):
            window_counter[s2[end]]-=1
            window_counter[s2[end+k]]+=1
            if window_counter[s2[end]] == 0:
                del window_counter[s2[end]]
            print(window_counter)
            if window_counter == s1_counter:
                return True
        return False