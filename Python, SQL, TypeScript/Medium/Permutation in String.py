class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])

        if s1_count == s2_count:
            return True

        for i in range(len(s1), len(s2)):
            s2_count[s2[i]] += 1
            s2_count[s2[i - len(s1)]] -= 1

            if s2_count[s2[i - len(s1)]] == 0:
                del s2_count[s2[i - len(s1)]]

            if s1_count == s2_count:
                return True

        return False