class Solution:
    def countEven(self, num: int) -> int:
        # Count the number of integers from 1 to num with an even digit sum
        count = 0
        for i in range(1, num + 1):
            if sum(int(digit) for digit in str(i)) % 2 == 0:
                count += 1
        return count