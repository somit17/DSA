class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "D":
                if stack:
                    val = stack[-1]
                    stack.append(int(val) * 2)
            elif op == "C":
                if stack:
                    stack.pop()
            elif op == "+":
                if stack:
                    val = int(stack[-1])+int(stack[-2])
                    stack.append(val)
            else:
                stack.append(op)

        result = 0
        while stack:
            result += int(stack.pop())
        return result    
        