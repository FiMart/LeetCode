class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        dp = [0] * (max(count) + 1)
        dp[1] = count[1]

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * count[i])

        return dp[-1]