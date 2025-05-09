class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        ans = 0
        for i in range(1, len(arrays)):
            ans = max(ans, abs(arrays[i][0] - max_val), abs(arrays[i][-1] - min_val))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return ans