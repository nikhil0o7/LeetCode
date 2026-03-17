class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        def backtrack(openN, closedN):
            if openN == closedN == n :
                ans.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if openN > closedN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0 , 0)
        return ans
        