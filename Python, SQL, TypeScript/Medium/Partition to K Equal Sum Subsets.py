class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k
        n = len(nums)
        dp = [False] * (1 << n)
        dp[0] = True
        subset_sum = [0] * (1 << n)

        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i) == 0:
                    new_mask = mask | (1 << i)
                    if dp[mask] and subset_sum[mask] + nums[i] <= target:
                        dp[new_mask] = True
                        subset_sum[new_mask] = (subset_sum[mask] + nums[i]) % target

        return dp[(1 << n) - 1]