class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * 26
        max_length = 1
        dp[ord(s[0]) - ord('a')] = 1

        for i in range(1, n):
            if (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                max_length += 1
            else:
                max_length = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], max_length)

        return sum(dp)