class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        idx = 0
        while idx  < min(len(word1),len(word2)):
            result.append(word1[idx])
            result.append(word2[idx])
            idx+=1
        if len(word1) > idx:
            result.append(word1[idx:])
        if len(word2) > idx:
            result.append(word2[idx:])
        return "".join(result)        