class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        min_num = min(nums)
        max_num = max(nums)
        return gcd(min_num, max_num)