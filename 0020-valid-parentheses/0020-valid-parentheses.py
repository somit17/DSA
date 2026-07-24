class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        for symbol in s:
            if symbol in hashmap:
                if stack and hashmap[symbol]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        return len(stack) == 0
        