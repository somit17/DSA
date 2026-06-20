class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            nptr = 0
            while nptr < n and haystack[i + nptr] == needle[nptr]:
                nptr+=1
            if nptr == n:
                return i
        return -1
            
