class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        count = 0
        for v in s:
            if v == '(':
                count += 1
                ans = max(ans, count)
            elif v == ')':
                count -= 1
        return ans