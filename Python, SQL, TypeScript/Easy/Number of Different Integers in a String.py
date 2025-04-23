class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        i, n = 0, len(word)
        while i < n:
            if word[i].isdigit():
                j = i
                while j < n and word[j].isdigit():
                    j += 1
                s.add(word[i:j].lstrip('0') or '0')
                i = j
            else:
                i += 1
        return len(s)