class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_square = 0
        count = 0
        
        for length, width in rectangles:
            square_side = min(length, width)
            if square_side > max_square:
                max_square = square_side
                count = 1
            elif square_side == max_square:
                count += 1
        
        return count