class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            if len(set(matrix[i])) != n or len(set(row[i] for row in matrix)) != n:
                return False
        return True