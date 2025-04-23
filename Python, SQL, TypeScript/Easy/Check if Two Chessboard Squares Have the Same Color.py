class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # Convert the coordinates to their respective row and column indices
        row1, col1 = ord(coordinate1[0]) - ord('a'), int(coordinate1[1]) - 1
        row2, col2 = ord(coordinate2[0]) - ord('a'), int(coordinate2[1]) - 1
        
        # Check if both squares are of the same color
        return (row1 + col1) % 2 == (row2 + col2) % 2