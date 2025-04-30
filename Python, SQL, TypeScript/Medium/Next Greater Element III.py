class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)

        # Step 1: Find the first decreasing element from the right
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # If no such element is found, return -1
        if i == -1:
            return -1

        # Step 2: Find the smallest element larger than digits[i] to the right of it
        j = length - 1
        while j > i and digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap the elements at indices i and j
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse the elements to the right of index i
        digits[i + 1:] = reversed(digits[i + 1:])

        # Convert back to integer and check for overflow
        result = int(''.join(digits))
        return result if result < 2**31 else -1