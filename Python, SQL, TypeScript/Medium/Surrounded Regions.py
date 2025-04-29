class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == 'X':
                return
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if (i in [0, rows - 1] or j in [0, cols - 1]) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'