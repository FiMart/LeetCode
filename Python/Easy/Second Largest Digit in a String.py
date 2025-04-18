class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for char in s:
            if char.isdigit():
                digits.add(int(char))
        sorted_digits = sorted(digits, reverse=True)
        return sorted_digits[1] if len(sorted_digits) > 1 else -1