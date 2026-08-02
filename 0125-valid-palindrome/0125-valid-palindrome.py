class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        window = []
        for c in s:
            if c.isalnum():
                window.append(c.lower())
        l=0
        r=len(window)-1
        print(window)
        while(l<=r):
            if window[l]!=window[r]:
                return False
            l+=1
            r-=1
        return True

        