class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        current_sum = sum(i * num for i, num in enumerate(nums))
        max_sum = current_sum

        for i in range(1, n):
            current_sum += total_sum - n * nums[n - i]
            max_sum = max(max_sum, current_sum)

        return max_sum