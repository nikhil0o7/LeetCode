class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            hours_spent = 0
            for p in piles:
                hours_spent += math.ceil(p/mid)

            if hours_spent <= h:
                res = min(res,mid)
                right = mid - 1
            else :
                left = mid + 1

        return res
        