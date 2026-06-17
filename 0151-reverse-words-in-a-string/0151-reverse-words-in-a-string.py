class Solution:
    def reverseWords(self, s: str) -> str:

        stack = []
        #print(s.split())
        for word in s.split():
                stack.append(word)
                #print(stack)
        result = []
        while stack:
            result.append(stack.pop())
        return " ".join(result)