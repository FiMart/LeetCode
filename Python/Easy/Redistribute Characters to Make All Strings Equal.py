class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter
        total_count = Counter()
        for word in words:
            total_count.update(word)
        return all(count % len(words) == 0 for count in total_count.values())