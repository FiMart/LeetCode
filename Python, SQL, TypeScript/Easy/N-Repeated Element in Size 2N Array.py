class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        count = Counter(nums)
        for num, freq in count.items():
            if freq == n:
                return num