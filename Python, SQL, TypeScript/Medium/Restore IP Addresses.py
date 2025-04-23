class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment: str) -> bool:
            # Check if the segment is valid: 0-255 and no leading zeros
            return 0 <= int(segment) <= 255 and (segment == "0" or segment[0] != "0")

        def backtrack(start: int, path: List[str]):
            # If we have 4 segments and we've used the entire string, add to results
            if len(path) == 4 and start == len(s):
                result.append(".".join(path))
                return

            # If we have 4 segments but haven't used the entire string, return
            if len(path) == 4:
                return

            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if is_valid(segment):
                        backtrack(start + length, path + [segment])

        result = []
        backtrack(0, [])
        return result