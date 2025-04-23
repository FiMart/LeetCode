class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        
        for r, c in indices:
            row[r] += 1
            col[c] += 1
        
        odd_rows = sum(1 for r in row if r % 2 == 1)
        odd_cols = sum(1 for c in col if c % 2 == 1)
        
        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols