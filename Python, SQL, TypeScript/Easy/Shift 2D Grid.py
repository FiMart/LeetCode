class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m * n
        flat_grid = [grid[i][j] for i in range(m) for j in range(n)]
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        return [[flat_grid[i * n + j] for j in range(n)] for i in range(m)]