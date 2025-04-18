class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for num in encoded:
            decoded.append(decoded[-1] ^ num)
        return decoded