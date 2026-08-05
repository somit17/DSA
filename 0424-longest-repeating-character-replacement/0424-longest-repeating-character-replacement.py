class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_map = Counter()
        start = 0
        max_freq = 0
        for end in range(len(s)):
            window_map[s[end]]+=1
            max_freq = max(max_freq,window_map[s[end]])

            if end - start + 1 - max_freq > k:
                window_map[s[start]]-=1
                start+=1
        return len(s) - start