class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        curr = 0
        num2 = 0
        num1 = 1
        for i in range(1, n):
            curr = num1 + num2
            num2 = num1
            num1 = curr
        return curr
        