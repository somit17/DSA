class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        def expand(l,r):
            while l>=0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        #Palindrome logic move from center
        for i in range(len(s)):
            even = expand(i,i)
            odd = expand(i,i+1)
            best = even if len(even) >= len(odd) else odd
            if len(best) > len(result):
                result = best
        return result