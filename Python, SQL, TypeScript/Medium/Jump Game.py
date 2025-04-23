class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = 0
        for i in range(n):
            if i > mx:
                return False
            mx = max(mx, i + nums[i])
        return True