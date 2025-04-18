class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = -1
        for x in nums:
            if x > 0 and -x in nums:
                ans = max(ans, x)
        return ans