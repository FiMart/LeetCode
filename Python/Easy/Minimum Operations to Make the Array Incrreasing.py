class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        prev_num = float('-inf')
        
        for num in nums:
            if num <= prev_num:
                operations += prev_num - num + 1
                num = prev_num + 1
            prev_num = num
        
        return operations