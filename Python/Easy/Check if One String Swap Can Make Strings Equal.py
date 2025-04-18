class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False

        diff = []
        for a, b in zip(s1, s2):
            if a != b:
                diff.append((a, b))
                if len(diff) > 2:
                    return False

        return len(diff) == 2 and diff[0] == diff[1][::-1]