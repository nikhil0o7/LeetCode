class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(curr, total, i):
            if total == target:
                ans.append(curr[:])
                return

            for j in range(i, len(candidates)):
                if total + candidates[j] <= target:
                    curr.append(candidates[j])
                    backtrack(curr, total + candidates[j], j)
                    curr.pop()

        ans = []
        backtrack([], 0, 0)
        return ans
        