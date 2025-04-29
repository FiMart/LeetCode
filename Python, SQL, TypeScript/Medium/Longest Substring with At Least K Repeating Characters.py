class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        if k <= 1:
            return len(s)
        
        char_count = Counter(s)
        for char, count in char_count.items():
            if count < k:
                return max(self.longestSubstring(substring, k) for substring in s.split(char))
        
        return len(s)