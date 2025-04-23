class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = mx = last = 0
        for i, x in enumerate(nums[:-1]):
            mx = max (mx, i + x)
            if i == last:
                ans += 1
                last = mx
        return ans