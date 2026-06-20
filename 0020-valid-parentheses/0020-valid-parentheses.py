class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for ch in s:
            if ch in my_dict:
                if len(stack) > 0 and my_dict[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
                
                