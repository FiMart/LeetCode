class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        n = len(s) // 2
        left_vowels = sum(1 for char in s[:n] if char in vowels)
        right_vowels = sum(1 for char in s[n:] if char in vowels)
        return left_vowels == right_vowels