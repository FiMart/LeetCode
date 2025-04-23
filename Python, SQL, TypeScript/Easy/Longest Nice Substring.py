class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub: str) -> bool:
            return len(set(sub.lower())) == len(set(sub)) // 2

        max_len = 0
        longest_sub = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_nice(s[i:j]) and (j - i) > max_len:
                    max_len = j - i
                    longest_sub = s[i:j]

        return longest_sub if max_len > 0 else ""