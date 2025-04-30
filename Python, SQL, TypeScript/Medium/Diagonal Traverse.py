class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        m, n = len(mat), len(mat[0])
        res = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                r = min(d, m - 1)
                c = d - r
                while r >= 0 and c < n:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                c = min(d, n - 1)
                r = d - c
                while c >= 0 and r < m:
                    res.append(mat[r][c])
                    r += 1
                    c -= 1
        return res