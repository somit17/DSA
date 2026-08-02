class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        result = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            key = tuple(count)
            if key not in hash_map:
                hash_map[key] =[]
            hash_map[key].append(s)
        
        for k,v in hash_map.items():
            result.append(v)
        return result