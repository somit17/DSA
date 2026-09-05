class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        window_set = set()
        max_count = 0

        for end in range(len(s)):

            while s[end] in window_set:
                window_set.remove(s[start])
                start+=1

            window_set.add(s[end])
            max_count = max(max_count,end - start + 1)
        return max_count