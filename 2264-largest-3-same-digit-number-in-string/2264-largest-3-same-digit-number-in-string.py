class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ' '
        
        for i in range(2,len(num)):
            if num[i]==num[i-1]==num[i-2]:
                result = max(result,num[i])
        if result == ' ':
            return ""
        return result * 3