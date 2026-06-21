class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def helper_function(left,right):
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        result = ""
        for i in range(len(s)):
            #Odd
            palindrome_odd = helper_function(i,i)
            #Even
            palindrome_even = helper_function(i,i+1)

            for palindrome in [palindrome_odd,palindrome_even]:
                if len(palindrome)>len(result):
                    result = palindrome
        return result