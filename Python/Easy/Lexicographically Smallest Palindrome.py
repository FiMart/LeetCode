class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        result = [''] * n
        for i in range(n // 2):
            result[i] = result[n - i - 1] = min(s[i], s[n - i - 1])
        if n % 2 == 1:
            result[n // 2] = s[n // 2]
        return ''.join(result)