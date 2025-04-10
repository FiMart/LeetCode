class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for w in words:
            t = Counter(w)
            if all(cnt[c] >= t[c] for c in t):
                ans += len(w)
        return ans