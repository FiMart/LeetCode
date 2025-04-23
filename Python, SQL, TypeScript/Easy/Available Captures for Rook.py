class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def is_valid(x, y):
            return 0 <= x < 8 and 0 <= y < 8 and board[x][y] != 'B'

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rook_pos = None

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_pos = (i, j)
                    break
            if rook_pos:
                break

        count = 0
        for dx, dy in directions:
            x, y = rook_pos
            while is_valid(x + dx, y + dy):
                x += dx
                y += dy
                if board[x][y] == 'p':
                    count += 1
                    break

        return count