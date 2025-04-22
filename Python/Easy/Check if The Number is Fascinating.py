class Solution:
    def isFascinating(self, n: int) -> bool:
        if n < 100:
            return False
        s = str(n) + str(n * 2) + str(n * 3)
        return len(s) == 9 and len(set(s)) == 9 and '0' not in s