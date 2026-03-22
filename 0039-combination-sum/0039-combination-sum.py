class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr[:])
                return

            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()
            backtrack(i + 1, curr, total)
        backtrack(0, [], 0)
        return res
        