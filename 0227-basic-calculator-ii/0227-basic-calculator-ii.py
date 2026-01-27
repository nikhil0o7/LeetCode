class Solution:
    def calculate(self, s: str) -> int:
        if not s: 
            return 0

        stack = [] 
        current = 0
        op = '+'
        s += '+'
        for ch in s:
            if ch.isdigit():
                current = current * 10 + int(ch)
            elif ch == ' ':
                pass
            else:
                if op == '+':
                    stack.append(current)
                elif op == '-':
                    stack.append(-current)
                elif op == '*':
                    stack.append(stack.pop() * current)
                elif op =='/':
                    prev = stack.pop()
                    stack.append(math.trunc(prev/current))
                op = ch
                current = 0 
        return sum(stack)
