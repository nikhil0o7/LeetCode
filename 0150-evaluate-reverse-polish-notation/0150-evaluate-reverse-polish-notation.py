class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                x1 =stack.pop()
                x2 = stack.pop()
                curr =  int(x1) + int(x2)
                stack.append(curr)
            elif t == "*":
                x1 = stack.pop()
                x2 = stack.pop()
                curr = int(x1) * int(x2)
                stack.append(curr)
            elif t == "-":
                x1 = int(stack.pop())
                x2 = int(stack.pop())
                curr = x2 - x1
                stack.append(curr)
            elif t == "/":
                x1 = int(stack.pop())
                x2 = int(stack.pop())
                curr = float(int(x2) / int(x1))
                stack.append(curr)
            else:
                stack.append(t)

        return int(float(stack[-1]))




        