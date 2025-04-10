class Solution:
    def sortString(self, s: str) -> str:
        cnt = Counter(s)
        result = []
        while cnt:
            for c in sorted(cnt.keys()):
                result.append(c)
                cnt[c] -= 1
                if cnt[c] == 0:
                    del cnt[c]
            for c in sorted(cnt.keys(), reverse=True):
                result.append(c)
                cnt[c] -= 1
                if cnt[c] == 0:
                    del cnt[c]
        return ''.join(result)