class Solution:
    def countAsterisks(self, s: str) -> int:
        ans, ok = 0, 1
        for c in s:
            if c == "|":
                ok = 1 - ok
            elif c == "*" and ok:
                ans += 1
        return ans