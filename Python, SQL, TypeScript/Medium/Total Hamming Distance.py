class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(32):
            count = sum((num >> i) & 1 for num in nums)
            total += count * (n - count)
        return total