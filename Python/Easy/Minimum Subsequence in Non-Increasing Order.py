class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        subsequence_sum = 0
        result = []
        
        for num in nums:
            subsequence_sum += num
            result.append(num)
            if subsequence_sum > total - subsequence_sum:
                break
        
        return result