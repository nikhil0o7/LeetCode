class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            hours_spent = 0
            for p in piles:
                hours_spent += math.ceil(p/mid)

            if hours_spent <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res

        