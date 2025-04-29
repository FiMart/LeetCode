class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(a, b, num):
            if not num:
                return True
            if a + b > 0 and num[0] == '0':
                return False
            for i in range(1, len(num) + 1):
                if a + b == int(num[:i]):
                    if dfs(b, a + b, num[i:]):
                        return True
            return False
        n = len(num)
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if num[0] == '0' and i > 1:
                    break
                if num[i] == '0' and j - i > 1:
                    break
                a = int(num[:i])
                b = int(num[i:j])
                if dfs(a, b, num[j:]):
                    return True
        return False