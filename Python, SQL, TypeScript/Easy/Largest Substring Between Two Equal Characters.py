class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        count = {}
        for i, v in enumerate(s):
            if v in count:
                ans = max(ans, i - count[v] - 1)
            else:
                count[v] = i
        return ans