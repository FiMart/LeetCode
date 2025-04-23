class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        current_sum = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            result[i] = current_sum
        
        return result