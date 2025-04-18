class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        min_num = nums[0]
        max_num = nums[-1]
        count = 0
        for num in nums:
            if num > min_num and num < max_num:
                count += 1
        return count