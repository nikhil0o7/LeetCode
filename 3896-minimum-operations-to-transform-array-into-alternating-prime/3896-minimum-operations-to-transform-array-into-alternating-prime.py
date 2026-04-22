class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False

            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
            
        even_indices = nums[::2]
        odd_indices = nums[1::2]
        operations = 0
        for k,v in enumerate(nums):
            if k % 2 == 0 :
                if not is_prime(v):
                    v = v + 1
                    operations += 1
                    while not is_prime(v):
                        v = v + 1
                        operations += 1
            else:
                if is_prime(v):
                    v = v + 1
                    operations += 1
                    while is_prime(v):
                        v = v + 1
                        operations += 1
        return operations
        