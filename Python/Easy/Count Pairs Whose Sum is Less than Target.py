class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n):
            j = bisect_left(nums, target - nums[i], i + 1)
            ans += j - i - 1
        return ans