class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Count the number of odd numbers in the range [low, high]
        return (high + 1) // 2 - low // 2