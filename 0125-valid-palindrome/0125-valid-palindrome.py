class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed_string = []

        for ch in s:
            if ch.isalnum():
                fixed_string.append(ch.lower())

        #print(fixed_string)
        return fixed_string == fixed_string[::-1]
        