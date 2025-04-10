class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky_numbers = [num for num, count in freq.items() if num == count]
        return max(lucky_numbers) if lucky_numbers else -1