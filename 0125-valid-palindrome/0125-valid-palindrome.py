class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for i in range(len(s)):
            if s[i].isalnum():
                result.append(s[i].lower())
        l,r = 0, len(result)-1
        while l<=r :
            if result[l]!=result[r]:
                return False
            l+=1
            r-=1
        return True
        print(result)
