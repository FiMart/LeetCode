class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum(num for num, cnt in count.items() if cnt == 1)