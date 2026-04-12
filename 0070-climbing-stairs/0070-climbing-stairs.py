class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 0
        step1 = 1
        step2 = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(2, n):
            curr = step1 + step2
            step1 = step2
            step2 = curr

        return curr
        