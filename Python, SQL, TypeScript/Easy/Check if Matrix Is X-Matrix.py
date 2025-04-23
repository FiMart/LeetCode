class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if (i == j or i + j == len(grid) - 1) and v == 0:
                    return False
                if (i != j and i + j != len(grid) - 1) and v != 0:
                    return False
        return True