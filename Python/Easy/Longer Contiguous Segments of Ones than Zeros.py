class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = max(len(x) for x in s.split('0'))
        zeros = max(len(x) for x in s.split('1'))
        return ones > zeros