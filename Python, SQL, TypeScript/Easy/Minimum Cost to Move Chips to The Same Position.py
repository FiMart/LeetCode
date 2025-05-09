class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum(1 for x in position if x % 2 == 1)
        even = len(position) - odd
        return min(odd, even)