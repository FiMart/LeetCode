class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        m, n = len(board), len(board[0])
        dx = [0, 0, -1, 1, -1, -1, 1, 1]
        dy = [-1, 1, 0, 0, -1, 1, -1, 1]

        def dfs(x: int, y: int) -> None:
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    cnt += 1
            if cnt > 0:
                board[x][y] = str(cnt)
                return
            board[x][y] = 'B'
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'E':
                    dfs(nx, ny)

        dfs(click[0], click[1])
        return board