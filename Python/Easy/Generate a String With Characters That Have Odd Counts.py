class Solution:
    def generateTheString(self, n: int) -> str:
        # If n is odd, we can use 'a' * n to generate a string with all characters having odd counts.
        # If n is even, we can use 'a' * (n - 1) + 'b' to generate a string with 'a' having odd count and 'b' having odd count.
        return 'a' * n if n % 2 == 1 else 'a' * (n - 1) + 'b'