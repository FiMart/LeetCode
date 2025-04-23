class Solution:
    def reformatNumber(self, number: str) -> str:
        # Remove all spaces and dashes from the number
        number = number.replace(" ", "").replace("-", "")
        
        # Initialize an empty list to store the formatted parts
        parts = []
        
        # Process the number in chunks of 3 or 2 digits
        i = 0
        while i < len(number):
            if len(number) - i > 4:
                parts.append(number[i:i+3])
                i += 3
            elif len(number) - i == 4:
                parts.append(number[i:i+2])
                parts.append(number[i+2:i+4])
                break
            else:
                parts.append(number[i:])
                break
        
        # Join the parts with dashes and return the result
        return "-".join(parts)