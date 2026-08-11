class Solution:
    def reverseVowels(self, s: str) -> str:
        map_set = {'a','A','e','E','I','i','o','O','u','U'}
        s = list(s)
        print(f'a - > {'a' in map_set}')
        start= 0 
        end = len(s) - 1
        while start <= end:
            if s[end] not in map_set:
                end-=1
            elif s[end] in map_set and s[start] in map_set:
                s[end],s[start] = s[start],s[end]
                end-=1
                start+=1
            else:
                start+=1
        return ''.join(s)

