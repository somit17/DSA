class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        count = 0
        for word in words:
            if set(word).issubset(allow):
                count+=1
        return count
        