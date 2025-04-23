from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        
        def is_sorted(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
        
        while not is_sorted(nums):
            min_sum = float('inf')
            min_index = -1
            
            for i in range(len(nums)-1):
                pair_sum = nums[i] + nums[i+1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i
            
            # Replace the pair with their sum
            nums = nums[:min_index] + [nums[min_index] + nums[min_index+1]] + nums[min_index+2:]
            operations += 1
        
        return operations
