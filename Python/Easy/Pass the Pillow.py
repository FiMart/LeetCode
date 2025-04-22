class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == 1:
            return 1
        time %= (n - 1) * 2
        if time < n - 1:
            return time + 1
        return n - (time - n + 1)