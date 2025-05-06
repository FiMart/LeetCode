class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            new_dp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for x, y in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                        ni, nj = i + x, j + y
                        if 0 <= ni < n and 0 <= nj < n:
                            new_dp[ni][nj] += dp[i][j] / 8.0
            dp = new_dp

        return sum(sum(row) for row in dp)