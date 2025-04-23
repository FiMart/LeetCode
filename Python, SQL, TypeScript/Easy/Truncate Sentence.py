class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        return ' '.join(words[:k]) if k < len(words) else s