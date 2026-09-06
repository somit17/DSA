class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}
        result = []

        for word in strs:
            count = [0] * 26
            for eachChar in word:
                count[ord(eachChar) - ord('a')]+=1
            key = tuple(count)
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(word)

        for k,v in hashMap.items():
            result.append(v)

        return result

        