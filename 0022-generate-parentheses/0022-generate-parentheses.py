class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(openN, closedN, curr) -> None:
            if len(curr) == n * 2:
                res.append("".join(curr[:]))
                return

            if len(curr) > n * 2:
                return

            if openN < n:
                curr.append("(")
                backtrack(openN + 1, closedN, curr)
                curr.pop()

            if closedN < openN:
                curr.append(")")
                backtrack(openN, closedN + 1, curr)
                curr.pop()

        res = []
        backtrack(0,0,[])
        return res

        