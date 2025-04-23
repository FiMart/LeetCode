class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_min = [min(row) for row in matrix]
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        return [matrix[i][j] for i in range(m) for j in range(n) if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]]