class Solution:
    def thousandSeparator(self, n: int) -> str:
        # Convert the integer to a string
        s = str(n)
        # Initialize an empty list to store the result
        result = []
        # Get the length of the string
        length = len(s)
        
        # Iterate through the string in reverse order
        for i in range(length):
            # Append the current character to the result list
            result.append(s[length - 1 - i])
            # If we have added 3 characters and it's not the last character, add a dot
            if (i + 1) % 3 == 0 and i != length - 1:
                result.append('.')
        
        # Reverse the result list and join it into a string
        return ''.join(result[::-1])