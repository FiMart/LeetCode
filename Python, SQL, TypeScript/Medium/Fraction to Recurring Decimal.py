class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))
        
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(result)
        
        result.append('.')
        
        # Fractional part
        remainder_map = {}
        index = 0
        
        while remainder != 0:
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], '(')
                result.append(')')
                break
            
            remainder_map[remainder] = len(result)
            remainder *= 10
            fractional_part = remainder // denominator
            result.append(str(fractional_part))
            remainder %= denominator
        
        return ''.join(result)