class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        ans = 0
        for i in range(len(num) - k + 1):
            if int(num[i:i + k]) != 0 and int(num) % int(num[i:i + k]) == 0:
                ans += 1
        return ans