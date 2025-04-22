class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                ans += i
            elif nums[i] == n:
                ans += n - 1 - i
        return ans + (nums.index(1) < nums.index(n)) - 1