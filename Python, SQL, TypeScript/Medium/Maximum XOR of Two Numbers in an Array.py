class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            candidate = max_xor | (1 << i)
            for prefix in prefixes:
                if prefix ^ candidate in prefixes:
                    max_xor = candidate
                    break
        return max_xor