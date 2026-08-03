class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_count = 0
        s_set = set()
        for end in range(0,len(s)):
            while s[end] in s_set:
                s_set.remove(s[start])
                start+=1

            s_set.add(s[end])
            max_count = max(max_count,end - start + 1)
        return max_count