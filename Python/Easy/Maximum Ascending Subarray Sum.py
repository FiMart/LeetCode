class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        prev_num = float('-inf')
        
        for num in nums:
            if num > prev_num:
                current_sum += num
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = num
            prev_num = num
        
        return max(max_sum, current_sum)