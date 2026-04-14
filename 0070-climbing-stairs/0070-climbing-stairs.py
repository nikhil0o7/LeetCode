class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        step1 = 1
        step2 = 2
        curr = step2
        for i in range(2, n):
            curr = step2 + step1
            step1 = step2
            step2 = curr

        return curr
        