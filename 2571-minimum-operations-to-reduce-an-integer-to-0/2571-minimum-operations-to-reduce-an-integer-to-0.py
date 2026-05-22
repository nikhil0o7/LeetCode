class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if n % 2 == 0:
                n >>= 1
            elif (n & 2) > 0:
                n += 1
                res +=1
            else:
                n >>= 2
                res +=1

        return res
            