class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for num in data:
            if count == 0:
                if (num >> 7) == 0b0:
                    continue
                elif (num >> 5) == 0b110:
                    count = 1
                elif (num >> 4) == 0b1110:
                    count = 2
                elif (num >> 3) == 0b11110:
                    count = 3
                else:
                    return False
            else:
                if (num >> 6) != 0b10:
                    return False
                count -= 1
        return count == 0