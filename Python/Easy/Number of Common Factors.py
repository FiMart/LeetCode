class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def gcd(x: int, y: int) -> int:
            while y:
                x, y = y, x % y
            return x

        g = gcd(a, b)
        return sum(g % i == 0 for i in range(1, g + 1))