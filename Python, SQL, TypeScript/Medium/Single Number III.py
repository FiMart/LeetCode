class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        # Find the rightmost set bit in xor
        rightmost_set_bit = xor & -xor

        # Divide numbers into two groups based on the rightmost set bit
        group1, group2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                group1 ^= num
            else:
                group2 ^= num

        return [group1, group2]