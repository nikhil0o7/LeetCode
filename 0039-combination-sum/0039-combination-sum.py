class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr, total, i):
            if total == target:
                res.append(curr[:])
                return

            for j in range(i, len(candidates)):
                if candidates[j] + total <= target:
                    curr.append(candidates[j])
                    backtrack(curr, total + candidates[j], j)
                    curr.pop()

        backtrack([], 0, 0)
        return res

        