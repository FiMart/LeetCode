class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = sum(1 for x in nums if x > 0)
        neg = sum(1 for x in nums if x < 0)
        return max(pos, neg)