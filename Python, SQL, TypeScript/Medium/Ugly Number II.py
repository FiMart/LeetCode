class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1

        i2, i3, i5 = 0, 0, 0
        next_2, next_3, next_5 = 2, 3, 5

        for i in range(1, n):
            next_ugly = min(next_2, next_3, next_5)
            ugly_numbers[i] = next_ugly

            if next_ugly == next_2:
                i2 += 1
                next_2 = ugly_numbers[i2] * 2
            if next_ugly == next_3:
                i3 += 1
                next_3 = ugly_numbers[i3] * 3
            if next_ugly == next_5:
                i5 += 1
                next_5 = ugly_numbers[i5] * 5

        return ugly_numbers[-1]