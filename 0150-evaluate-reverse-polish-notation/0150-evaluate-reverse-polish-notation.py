class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
             if ch == '+':
                x = stack.pop()
                y = stack.pop()
                ans = int(y) + int(x)
                stack.append(ans)
             elif ch == '*':
                x = stack.pop()
                y = stack.pop()
                ans = int(y) * int(x)
                stack.append(ans)
             elif ch == '-':
                x = stack.pop()
                y = stack.pop()
                ans = int(y) - int(x)
                stack.append(ans)
             elif ch == '/':
                x = stack.pop()
                y = stack.pop()
                ans = float(int(y) / int(x))
                stack.append(ans)
             else:
                stack.append(ch)

        return int(float(stack[-1]))
        