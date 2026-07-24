class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_strs = s.split()
        print(split_strs)
        return len(split_strs[-1])
        