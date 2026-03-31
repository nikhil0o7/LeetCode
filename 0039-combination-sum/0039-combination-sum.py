class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, total, i) -> None:
            if total == target:
                ans.append(curr[:])
                return 
                
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(curr, total + candidates[i], i)
            curr.pop()

            backtrack(curr, total, i + 1)

        backtrack([], 0, 0)
        return ans





        