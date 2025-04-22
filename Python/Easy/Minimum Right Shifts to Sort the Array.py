from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Check if already sorted
        if nums == sorted(nums):
            return 0
        
        for shift in range(1, n):
            shifted = nums[-shift:] + nums[:-shift]
            if shifted == sorted(nums):
                return shift
        
        return -1
