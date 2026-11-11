class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = Counter(s)
        result = 0
        oddFreq = False
        for k,v in hashmap.items():
            #print(f'{k} - > {v}')
            if v & 1 == 0:
                result+=v
            else:
                result+=v-1
                oddFreq = True
            
        return result+1 if oddFreq else result