class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for i in range(25, -1, -1):
            if chr(i + 65) in s and chr(i + 97) in s:
                return chr(i + 65)
        return ''   