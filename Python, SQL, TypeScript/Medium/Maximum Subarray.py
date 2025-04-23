class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = mx = nums[0]
        for x in nums[1:]:
            mx = max(mx + x, x)
            ans = max(ans, mx)
        return ans