class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_str = s.split()
        return len(list_str[-1])