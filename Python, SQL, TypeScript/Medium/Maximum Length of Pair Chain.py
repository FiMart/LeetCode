class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans = 0
        prev_end = float('-inf')
        for start, end in pairs:
            if start > prev_end:
                ans += 1
                prev_end = end
        return ans