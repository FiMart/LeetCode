class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # If there are still digits to remove, remove from the end
        stack = stack[:-k] if k else stack
        # Remove leading zeros and return the result
        return ''.join(stack).lstrip('0') or '0'