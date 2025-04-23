class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')
        for i in range(n):
            if words[i] == target:
                ans = min(ans, min(abs(i - startIndex), n - abs(i - startIndex)))
        return ans if ans != float('inf') else -1