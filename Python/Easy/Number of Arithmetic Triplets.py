class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums = set(nums)
        count = 0
        for num in nums:
            if num + diff in nums and num + 2 * diff in nums:
                count += 1
        return count