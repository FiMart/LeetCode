class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = [0] * 10
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])
            if color == "R":
                cnt[rod] |= 1 << 0
            elif color == "G":
                cnt[rod] |= 1 << 1
            else:
                cnt[rod] |= 1 << 2
        return sum(c == 7 for c in cnt)