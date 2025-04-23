class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])
        special_positions = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_positions += 1

        return special_positions