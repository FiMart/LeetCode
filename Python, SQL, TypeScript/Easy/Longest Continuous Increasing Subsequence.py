class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = cnt = 1
        for i, x in enumerate(nums[1:]):
            if x > nums[i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans