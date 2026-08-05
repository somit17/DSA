class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        start = 0
        count = 0
        window_map = Counter()
        for end in range(len(s)):
            leading_char = s[end]
            window_map[leading_char] = window_map.get(leading_char,0) + 1 
            while len(window_map) == 3:
                count += n - end
                trailing_char = s[start]
                window_map[trailing_char]-=1
                if window_map[trailing_char] == 0:
                    del window_map[trailing_char]
                start+=1
        return count
