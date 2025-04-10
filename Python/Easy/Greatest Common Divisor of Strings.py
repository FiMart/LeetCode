class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def check(s1: str, s2: str) -> bool:
            if len(s1) % len(s2) != 0:
                return False
            for i in range(len(s1) // len(s2)):
                if s1[i * len(s2):(i + 1) * len(s2)] != s2:
                    return False
            return True

        g = gcd(len(str1), len(str2))
        candidate = str1[:g]
        if check(str1, candidate) and check(str2, candidate):
            return candidate
        return ""