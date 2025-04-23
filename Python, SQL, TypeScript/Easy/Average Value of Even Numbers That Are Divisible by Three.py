class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = [x for x in nums if x % 2 == 0 and x % 3 == 0]
        return sum(nums) // len(nums) if nums else 0