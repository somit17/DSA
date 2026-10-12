class Solution:
    def isPalindrome(self, s: str) -> bool:
        refactored_string = ''.join([ch.lower() for ch in s if ch.isalnum()])
        return refactored_string == refactored_string[::-1]
        #print(refactored_string)
        # l,r = 0,len(refactored_string)-1
        # while l<=r:
        #     if refactored_string[l]!=refactored_string[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True
        