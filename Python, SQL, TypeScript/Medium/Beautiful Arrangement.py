class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(i, visited):
            if i == n + 1:
                return 1
            ans = 0
            for j in range(1, n + 1):
                if not visited[j] and (i % j == 0 or j % i == 0):
                    visited[j] = True
                    ans += dfs(i + 1, visited)
                    visited[j] = False
            return ans

        visited = [False] * (n + 1)
        return dfs(1, visited)