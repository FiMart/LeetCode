class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Check if the string is a palindrome
        if s == s[::-1]:
            # If it is a palindrome, we can remove it in one step
            return 1
        else:
            # If it is not a palindrome, we can remove all 'a's and all 'b's in two steps
            return 2