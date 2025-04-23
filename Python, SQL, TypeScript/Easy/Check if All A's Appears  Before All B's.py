class Solution:
    def checkString(self, s: str) -> bool:
        # Check if all 'a's appear before all 'b's in the string s
        # This is done by checking if 'ba' is present in the string
        return 'ba' not in s