class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = Counter(s)
        for i,char in enumerate(s):
            if hash_map[char]==1:
                return i
        return -1

        