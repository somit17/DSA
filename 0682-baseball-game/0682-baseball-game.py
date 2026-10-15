class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == 'C':
                if stack:
                    stack.pop()

            elif operation == 'D':
                if stack:
                    num = stack[-1]
                    stack.append(2 * num)

            elif operation == '+':
                num1 = stack[-1] if stack else 0
                num2 = stack[-2] if stack else 0
                stack.append(num1+num2)

            else:
                stack.append(int(operation))

        return sum(stack)