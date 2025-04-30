class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        memo = {}

        def canWin(remaining, total):
            if remaining in memo:
                return memo[remaining]
            for i in range(1, maxChoosableInteger + 1):
                if remaining & (1 << i) and total + i >= desiredTotal:
                    memo[remaining] = True
                    return True
                if remaining & (1 << i) and not canWin(remaining ^ (1 << i), total + i):
                    memo[remaining] = True
                    return True
            memo[remaining] = False
            return False

        return canWin((1 << (maxChoosableInteger + 1)) - 2, 0)