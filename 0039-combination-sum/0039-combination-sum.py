class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, total, curr):
            if total == target:
                res.append(curr[:])
                return


            for j in range(i, len(candidates)):
                if total + candidates[j] >  target:
                    break
                curr.append(candidates[j])
                backtrack(j, total + candidates[j], curr)
                curr.pop()


        backtrack(0, 0, [])
        return res





        