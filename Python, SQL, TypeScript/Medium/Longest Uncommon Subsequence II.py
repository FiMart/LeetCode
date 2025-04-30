class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s1: str, s2: str) -> bool:
            i = 0
            for c in s2:
                if i < len(s1) and s1[i] == c:
                    i += 1
            return i == len(s1)

        max_length = -1
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, strs[j]) for j in range(len(strs)) if j != i):
                max_length = max(max_length, len(s))
        return max_length