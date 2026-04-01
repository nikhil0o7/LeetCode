class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i, curr) -> None:
            if k == len(curr):
                ans.append(curr[:])
                return

            for j in range(i, n + 1):
                curr.append(j)
                backtrack(j + 1, curr)
                curr.pop()

        backtrack(1, [])
        return ans

        