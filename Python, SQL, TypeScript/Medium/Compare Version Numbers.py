class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.')))

        # Compare each part of the version numbers
        for v1, v2 in zip(v1_parts, v2_parts):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        # If all compared parts are equal, check the lengths of the version numbers
        if len(v1_parts) < len(v2_parts):
            return -1 if any(v > 0 for v in v2_parts[len(v1_parts):]) else 0
        elif len(v1_parts) > len(v2_parts):
            return 1 if any(v > 0 for v in v1_parts[len(v2_parts):]) else 0

        return 0