class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        if target == 0 or target == x or target == y or target == x + y:
            return True
        if x == 0 or y == 0:
            return False
        return target % math.gcd(x, y) == 0