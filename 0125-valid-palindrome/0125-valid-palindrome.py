class Solution:
    def isPalindrome(self, s: str) -> bool:
        perfect_str = []
        for ch in s:
            if ch.isalnum():
                perfect_str.append(ch.lower())
        print(perfect_str)
        l = 0
        r = len(perfect_str)-1
        while(l < r):
            if perfect_str[l]!=perfect_str[r]:
                return False
            l+=1
            r-=1
        return True