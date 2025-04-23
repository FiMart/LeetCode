class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        for c in set(cnt1.keys()).union(set(cnt2.keys())):
            if abs(cnt1[c] - cnt2[c]) > 3:
                return False
        return True