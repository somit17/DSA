class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == 'C':
                if stack and len(stack) > 0:
                    stack.pop()

            elif operation == 'D':
                if stack and len(stack) > 0:
                    num = stack[-1]
                    stack.append(2 * num)

            elif operation == '+':
                num1 = stack[-1] if stack and len(stack) > 0 else 0
                num2 = stack[-2] if stack and len(stack) > 0 else 0
                stack.append(num1+num2)

            else:
                stack.append(int(operation))

        return sum(stack)