class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for k in range(1, len(sequence) // len(word) + 1):
            if word * k not in sequence:
                return k - 1
        return len(sequence) // len(word)