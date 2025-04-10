class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_one = -1
        for i in range(32):
            if n & (1 << i):
                if last_one != -1:
                    max_gap = max(max_gap, i - last_one)
                last_one = i
        return max_gap if max_gap else 0