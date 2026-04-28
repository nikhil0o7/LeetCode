class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, total , curr):
            if total == target:
                res.append(curr[:])
                return
            if total > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            backtrack(i + 1, total + candidates[i], curr)
            curr.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i = i + 1

            backtrack(i+ 1, total, curr)
        

        backtrack(0, 0, [])
        return res