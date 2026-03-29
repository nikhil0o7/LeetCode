class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        stack = []
        for ch in s:
            if ch in stack:
                if stack and stack[-1] == d[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        print(stack)
        return len(stack) == 0



