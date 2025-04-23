class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[::2])
        odd = sorted(nums[1::2], reverse=True)
        return [even[i // 2] if i % 2 == 0 else odd[i // 2] for i in range(len(nums))]