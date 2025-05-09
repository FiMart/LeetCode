class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 0
        div = 1
        while x >= 10 * div:
            div *= 10
        while x:
            if x // div != x % 10:
                return 0
            x = (x % div) // 10
            div = div / 100
        return 1