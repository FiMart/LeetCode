class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        min_num = min(nums)
        if max_num - min_num <= 2 * k:
            return 0
        else:
            return max_num - min_num - 2 * k