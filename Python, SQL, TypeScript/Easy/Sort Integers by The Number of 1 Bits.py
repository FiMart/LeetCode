class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort by the number of 1 bits, then by the value itself
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))