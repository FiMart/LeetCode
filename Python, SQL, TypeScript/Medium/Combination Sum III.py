class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start: int, k: int, n: int, path: List[int], res: List[List[int]]):
            if k == 0 and n == 0:
                res.append(path.copy())
                return
            if k < 0 or n < 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, k - 1, n - i, path, res)
                path.pop()

        res = []
        backtrack(1, k, n, [], res)
        return res