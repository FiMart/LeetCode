class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    ans += 2 + grid[i][j] * 4
                    if i > 0:
                        ans -= min(grid[i][j], grid[i - 1][j]) * 2
                    if j > 0:
                        ans -= min(grid[i][j], grid[i][j - 1]) * 2
        return ans