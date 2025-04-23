class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        max_row = -1
        for i in range(len(mat)):
            ones_count = sum(mat[i])
            if ones_count > max_ones:
                max_ones = ones_count
                max_row = i
        return [max_row, max_ones]