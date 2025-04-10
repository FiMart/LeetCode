class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n < 2:
            return 1
        
        # Sieve of Eratosthenes to count prime numbers up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        prime_count = sum(is_prime)
        non_prime_count = n - prime_count
        
        # Calculate factorial modulo 10^9 + 7
        MOD = 10**9 + 7
        
        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result = (result * i) % MOD
            return result
        
        return (factorial(prime_count) * factorial(non_prime_count)) % MOD