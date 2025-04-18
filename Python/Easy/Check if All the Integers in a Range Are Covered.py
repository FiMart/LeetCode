class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        s = 0
        for i, x in enumerate(diff):
            s += x
            if left <= i <= right and s == 0:
                return False
        return True