class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        stack = []
        first_char = sentence[0]

        for i in range(len(sentence)):
            if sentence[i] == ' ':
                prev_last = stack.pop()
                if sentence[i+1]!=prev_last:
                    return False
            else:
                stack.append(sentence[i])

        return stack[-1] == first_char