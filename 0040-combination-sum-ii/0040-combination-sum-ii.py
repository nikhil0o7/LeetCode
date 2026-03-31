class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, curr, total) -> None:
            if total == target:
                res.append(curr[:])
                return

            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])
            curr.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i +=1 

            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return res
        