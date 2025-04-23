class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = defaultdict(int)
        for i, c in enumerate(s):
            if d[c] == 0:
                d[c] = i + 1
            else:
                if i - d[c] != distance[ord(c) - ord('a')]:
                    return False
        return True