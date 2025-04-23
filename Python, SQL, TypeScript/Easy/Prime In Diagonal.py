class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        max_prime = 0
        n = len(nums)
        for i in range(n):
            if is_prime(nums[i][i]):
                max_prime = max(max_prime, nums[i][i])
            if is_prime(nums[i][n - i - 1]):
                max_prime = max(max_prime, nums[i][n - i - 1])
        return max_prime