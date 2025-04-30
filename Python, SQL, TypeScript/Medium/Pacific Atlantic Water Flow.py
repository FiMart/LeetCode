class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def dfs(x, y, visited):
            visited[x][y] = True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, visited)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        return [[i, j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]