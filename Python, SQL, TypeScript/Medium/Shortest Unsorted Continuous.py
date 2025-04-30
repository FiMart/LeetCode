class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        # Find the first element from the left that is out of order
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        
        # If we reached the end, the array is already sorted
        if left == n - 1:
            return 0
        
        # Find the first element from the right that is out of order
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        
        # Find the minimum and maximum in the unsorted subarray
        min_unsorted = min(nums[left:right + 1])
        max_unsorted = max(nums[left:right + 1])
        
        # Expand the left boundary if needed
        while left > 0 and nums[left - 1] > min_unsorted:
            left -= 1
        
        # Expand the right boundary if needed
        while right < n - 1 and nums[right + 1] < max_unsorted:
            right += 1
        
        return right - left + 1