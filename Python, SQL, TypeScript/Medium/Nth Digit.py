class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, count, start = 1, 9, 1
        while n > digit * count:
            n -= digit * count
            digit += 1
            count *= 10
            start *= 10
        start += (n - 1) // digit
        return int(str(start)[(n - 1) % digit])