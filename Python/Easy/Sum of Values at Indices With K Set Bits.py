class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, n in enumerate(nums):
            if bin(i).count('1') == k:
                ans += n
        return ans