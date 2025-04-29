class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        indices = [0] * len(primes)
        next_ugly = [p for p in primes]

        for i in range(1, n):
            next_ugly_index = min(range(len(next_ugly)), key=lambda x: next_ugly[x])
            ugly[i] = next_ugly[next_ugly_index]

            for j in range(len(primes)):
                if ugly[i] == next_ugly[j]:
                    indices[j] += 1
                    next_ugly[j] = ugly[indices[j]] * primes[j]

        return ugly[-1]