class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(x, y, moves):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if moves == 0:
                return 0
            return (dfs(x + 1, y, moves - 1) +
                    dfs(x - 1, y, moves - 1) +
                    dfs(x, y + 1, moves - 1) +
                    dfs(x, y - 1, moves - 1)) % (10**9 + 7)
        return dfs(startRow, startColumn, maxMove)