class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        freq = Counter(nums)
        # Sort the numbers by frequency (ascending) and then by value (descending)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        return sorted_nums