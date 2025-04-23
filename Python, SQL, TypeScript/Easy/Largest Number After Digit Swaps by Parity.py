class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        even = sorted([int(d) for d in num if int(d) % 2 == 0], reverse=True)
        odd = sorted([int(d) for d in num if int(d) % 2 == 1], reverse=True)
        ans = ''
        for d in num:
            if int(d) % 2 == 0:
                ans += str(even.pop(0))
            else:
                ans += str(odd.pop(0))
        return int(ans)