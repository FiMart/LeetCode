class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(num: int) -> None:
            if num > n:
                return
            result.append(num)
            for i in range(10):
                next_num = num * 10 + i
                if next_num > n:
                    break
                dfs(next_num)

        result = []
        for i in range(1, 10):
            dfs(i)
        return result