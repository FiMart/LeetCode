class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        ans = [[0] * (m - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(m - 2):
                ans[i][j] = max(max(grid[i][j:j + 3]), max(grid[i + 1][j:j + 3]), max(grid[i + 2][j:j + 3]))
        return ans