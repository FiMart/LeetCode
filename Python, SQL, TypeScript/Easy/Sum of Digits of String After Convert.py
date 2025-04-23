class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert each character to its corresponding number and concatenate them
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Convert the concatenated string to an integer
        num = int(num_str)
        
        # Perform the digit sum operation k times
        for _ in range(k):
            num = sum(int(digit) for digit in str(num))
        
        return num