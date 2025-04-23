class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            return "-" + self.convertToBase7(-num)
        base7_digits = []
        
        while num > 0:
            base7_digits.append(str(num % 7))
            num //= 7
        return "".join(reversed(base7_digits))